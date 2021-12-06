from src.modelos.modelos import Task, TaskSchema
import bcrypt
from flask_restful import Resource
from ..constantes.constantes import AudioFormat, AudioContentType, TaskStatus
from ..tareas.tareas import process_uploaded_task
from ..modelos import db, User, S3Client
from flask import request
from sqlalchemy.exc import IntegrityError
from flask_jwt_extended import jwt_required, create_access_token, get_jwt_identity
from datetime import datetime
from celery import Celery
import redis
import bcrypt
from flask import send_file, send_from_directory
from sqlalchemy.sql import exists
import os
import glob

task_schema = TaskSchema()

task_schema = TaskSchema()

class VistaSignIn(Resource):

    def post(self):
        password1 = request.json["password1"]
        password2 = request.json["password2"]
        email = request.json["email"]
        if password1 != password2:
            return {"message": "Passwords must match in order to Sign-In"}, 403

        ##password1 = bcrypt.hashpw((password1).encode('utf-8'), bcrypt.gensalt())
        exist_email = User.query.filter_by(email=email).first() is not None
        if exist_email:
            return {"message": "This Email match an existent account.Try again!"}, 403
        new_user = User(username=request.json["username"], password1=password1, email=email)
        access_token = create_access_token(identity=request.json["username"])
        db.session.add(new_user)
        db.session.commit()
        return {"message": "user created successfully", "access_token": access_token}

    def delete(self, user_id):
        user = User.query.get_or_404(user_id)
        db.session.delete(user)
        db.session.commit()
        return '', 204


class VistaLogIn(Resource):
    def get(self):
        return "pong"

    def post(self):
        u_username = request.json["username"]
        u_password1 = request.json["password1"]
        user = User.query.filter_by(username=u_username).first()
        db.session.commit()

        if user is None:
            return "The username do not exist", 404

        ##if not bcrypt.checkpw(u_password1.encode('utf8'), user.password1):
            ##return "Incorrect password"

        else:
            access_token = create_access_token(identity=user.username)
            return {"message": "Access granted", "username": {"username": user.username, "id": user.id},
                    "access_token": access_token}


class VistaLoadFile(Resource):
    @jwt_required()
    def post(self):
        file = request.files['fileName']
        new_format = request.form["newFormat"]
        file_list = file.filename.split('.')
        try:
            user_name = User.query.filter_by(username=get_jwt_identity()).first().username
            new_file_name = f"{file_list[0]}.{new_format}"
            file.save(f"/nfs/general/files/{user_name}.{file_list[1]}")
            os.system(f'ffmpeg -i /nfs/general/files/{user_name}.{file_list[1]} /nfs/general/files/{new_file_name}')
        except Exception as e:
            return {"message": str(e)}, 404
        try:
            return send_file(f"/nfs/general/files/{new_file_name}", as_attachment=True)
        finally:
            os.remove(f"/nfs/general/files/{user_name}.{file_list[1]}")
            os.remove(f"/nfs/general/files/{new_file_name}")

class VistaTask(Resource):
    @jwt_required()
    def get(self, id_task):
        task = Task.query.get_or_404(id_task)
        return task_schema.dump(task)

    @jwt_required()
    def put(self, id_task):
        new_format = request.form['newFormat']
        if new_format.lower() not in (AudioFormat.all()):
            return {'error': f'New format should be one of {AudioFormat.all()}'}, 400

        task = Task.query.get_or_404(id_task)
        try:
            os.remove(f"/nfs/general/files/{task.converted_filename}")

            task.status = TaskStatus.UPLOADED.value
            task.converted_filename = None
            task.new_format = new_format
            db.session.add(task)
            db.session.commit()
            process_uploaded_task.delay(task_schema.dump(task))
        except Exception as e:
            return {'error': str(e)}

        return {'result': 'The conversion task was updated'}

    @jwt_required()
    def delete(self, id_task):
        task = Task.query.get_or_404(id_task)
        db.session.delete(task)
        db.session.commit()
        return 'Task '+str(id_task)+' has been eliminated'

class VistaFile(Resource):
    @jwt_required()
    def get(self, filename):
        if str(filename).split('.')[1] not in (AudioFormat.all()):
            return {'error': f'File format should be one of {AudioFormat.all()}'}, 400
        try:
            recordings_bucket = 'recordingsbucket01'
            client = S3Client().client
            tasks = db.session.query(Task).filter(Task.original_filename == filename)
            client.download_file(recordings_bucket,f'src/files/{tasks[0].filename}', f'src/files/{tasks[0].filename}')
            return send_from_directory("/app/src/files/", tasks[0].filename, as_attachment=True)
        except Exception as e:
            return {"message": "the file to recover not found " + tasks[0].filename}, 404