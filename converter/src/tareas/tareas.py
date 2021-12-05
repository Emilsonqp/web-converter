import os

from celery import Celery

from src import create_app
from ..constantes.constantes import TaskStatus

from ..modelos import Task, db, User , S3Client

from ..servicios.mail_service import send_mail_processed_file

#celery_app = Celery(__name__, broker='redis://localhost:6379/0')

celery_app = Celery(__name__, broker="sqs://sqs.us-east-1.amazonaws.com/449728648057/celery")
recordings_bucket = 'recordingsbucket01'

@celery_app.task(name="process_uploaded_task")
def process_uploaded_task(task: dict):
    app = create_app('default')
    client = S3Client().client
    with app.app_context():
        app.debug = True
        db.init_app(app)

        filename = task['filename']
        new_format = task['new_format']
        file_list = filename.split('.')
        new_file_name = f'{file_list[0]}.{new_format}'
        print("pre conversion")
        client.download_file(recordings_bucket,f'src/files/{task["filename"]}', f'src/files/{task["filename"]}')
        new_path = f'src/files/{new_file_name}'
        os.system(f'sudo ffmpeg -i src/files/{task["filename"]} {new_path}')
        client.upload_file(new_path,recordings_bucket,new_path)
        print("post conversion")
        task = Task.query.get(task['id'])
        task.status = TaskStatus.PROCESSED.value
        task.converted_filename = new_file_name
        db.session.add(task)
        db.session.commit()

        user = User.query.filter_by(id=task.user_id).first()

        if os.environ.get('SEND_MAIL', False):
            send_mail_processed_file(
                user.email,
                filename,
                new_format,
                new_file_name,
            )