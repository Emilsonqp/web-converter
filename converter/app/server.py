from flask import Flask

def create_app(config_name):
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://dqbxzwmkgoeqzp:b48d9b0f64812d3c53ed6bad86874b7c2f1309aaf97d4a1c40703cec29e92156@ec2-3-230-219-251.compute-1.amazonaws.com:5432/d2917gi1aubhfl'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['JWT_SECRET_KEY'] = 'ROCK&ROLL_TRAIN_ACDC'
    app.config['PROPAGATE_EXCEPTION'] = True

    return app
