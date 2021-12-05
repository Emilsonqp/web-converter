from flask import Flask

def create_app(config_name):
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://admin:password@database12.cnyx6ur7iubn.us-east-1.rds.amazonaws.com:3306/database12'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['JWT_SECRET_KEY'] = 'ROCK&ROLL_TRAIN_ACDC'
    app.config['PROPAGATE_EXCEPTION'] = True

    return app
