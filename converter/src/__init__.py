from flask import Flask

def create_app(config_name):
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://twtuknjznpifgw:7e3a3f98cca6b2f78dceb447adbd4ef4664f7ec923791baab75c6931b2099765@ec2-18-210-159-154.compute-1.amazonaws.com:5432/d9biglev8tc8tb'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['JWT_SECRET_KEY'] = 'ROCK&ROLL_TRAIN_ACDC'
    app.config['PROPAGATE_EXCEPTION'] = True

    return app
