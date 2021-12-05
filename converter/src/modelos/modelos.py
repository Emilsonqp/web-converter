from flask_sqlalchemy import SQLAlchemy
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from sqlalchemy import text, ForeignKey
from sqlalchemy.orm import relationship
import boto3
from src.constantes.constantes import TaskStatus, S3CustomKeys


db = SQLAlchemy()


class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50))
    password1 = db.Column(db.String(100))
    email = db.Column(db.String(100))
    tasks = relationship('Task')


class Task(db.Model):
    __tablename__ = 'task'
    id = db.Column(db.Integer, primary_key=True)
    filename = db.Column(db.String(150))
    new_format = db.Column(db.String(50))
    timestamp = db.Column(db.TIMESTAMP, server_default=text('CURRENT_TIMESTAMP'))
    status = db.Column(db.String(50), server_default=TaskStatus.UPLOADED.value)
    converted_filename = db.Column(db.String(150))
    user_id = db.Column(db.Integer, ForeignKey('user.id'))
    original_filename = db.Column(db.String(150))


class S3Client:
    def __init__(self):
        self.client = boto3.client('s3', aws_access_key_id     = S3CustomKeys.AWS_ACCESS_KEY_ID.value,
                                         aws_secret_access_key = S3CustomKeys.AWS_SECRET_ACCESS_KEY.value,
                                         aws_session_token     = S3CustomKeys.AWS_SESSION_TOKEN.value)



class TaskSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Task
        include_relationships = True
        load_instance = True
