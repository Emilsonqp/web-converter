from flask_restful import Resource
from flask import request
from flask_jwt_extended import jwt_required, get_jwt_identity
from marshmallow import Schema, fields, validate
from time import time
from celery import Celery

from ..constantes.constantes import AudioFormat, AudioContentType

from ..modelos import db, Task, TaskSchema, User , S3Client
import boto3
import os


# celery_app = Celery('gestor',
#                     broker=f"sqs://{queue_url}",
#                     backend='rpc://',
#                     task_default_queue=f"{queue_name}")

celery = Celery(__name__, broker="sqs://ASIAWRNPKSN4WDZCDCT3:kNiQ9l6B/DXmXs4JRJY07bpMGQ2QscN93HDnLKwH@sqs.us-east-1.amazonaws.com/449728648057/celery")

recordings_bucket = 'recordingsbucket01'

@celery.task(name="process_uploaded_task")
def process_uploaded_task(cancion_json):
    pass


class TaskGetSchema(Schema):
    max = fields.Int(validate=validate.Range(min=1))
    order = fields.Int(required=True, validate=validate.OneOf([0, 1]))


task_schema = TaskSchema()
task_get_schema = TaskGetSchema()


class VistaTasks(Resource):
    @jwt_required()
    def get(self):
        errors = task_get_schema.validate(request.args)
        if errors:
            return str(errors), 400

        query_params = request.args
        max = query_params.get('max')
        order = int(query_params.get('order', 0))
        order_by = Task.id.asc() if order == 0 else Task.id.desc()
        user_id = User.query.filter_by(username=get_jwt_identity()).first().id
        tasks = Task.query.filter_by(user_id=user_id).order_by(order_by).limit(max).all()

        return [task_schema.dump(t) for t in tasks]

    @jwt_required()
    def post(self):
        client = S3Client().client
        file = request.files['fileName']
        if file is None:
            return {'error': 'Please send a valid file'}, 400

        if file.content_type not in (AudioContentType.all()):
            return {'error': f'File format should be one of {AudioFormat.all()}'}, 400

        new_format = request.form['newFormat']
        if new_format.lower() not in (AudioFormat.all()):
            return {'error': f'New format should be one of {AudioFormat.all()}'}, 400

        file_list = file.filename.split('.')
        filename = f'{file_list[0]}-{int(time())}.{file_list[1]}'
        path = f'/home/emilsonqp/flask_application/heroku/web-converter/converter/src/files/{filename}'
        user_id = User.query.filter_by(username=get_jwt_identity()).first().id
        new_task = Task(filename=filename, new_format=new_format, user_id=user_id, original_filename=file.filename)
        db.session.add(new_task)
        db.session.commit()
        try:
            file.save(path)
            client.upload_file(path,recordings_bucket,path)
            process_uploaded_task.delay(task_schema.dump(new_task))
            os.remove(path)
        except Exception as e:
            return {'error': str(e)}

        return {'result': 'The conversion task was created'}
