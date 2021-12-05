from flask import Flask

def create_app(config_name):
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://hlfjayuvhpajqc:d79309f920e2f57d688fc6a415d60d81b603d00eaf1e5f5127722bf611988e24@ec2-3-230-219-251.compute-1.amazonaws.com:5432/do2vr4v7ha391'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['JWT_SECRET_KEY'] = 'ROCK&ROLL_TRAIN_ACDC'
    app.config['PROPAGATE_EXCEPTION'] = True

    return app
