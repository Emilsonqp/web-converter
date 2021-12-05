from flask import Flask

def create_app(config_name):
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://bevoakcksbasdr:8a57bd971a47321682060ce14ac5fd30d2d4d33c1e6805131ec86d9385326b57@ec2-52-7-30-112.compute-1.amazonaws.com:5432/d8g4mmsr92f0ej'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['JWT_SECRET_KEY'] = 'ROCK&ROLL_TRAIN_ACDC'
    app.config['PROPAGATE_EXCEPTION'] = True

    return app
