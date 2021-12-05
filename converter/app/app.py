from server import create_app
from modelos import db
from flask_restful import Api
from .vistas import VistaLogIn, VistaSignIn, VistaLoadFile, VistaTask, VistaFile
from flask_jwt_extended import JWTManager
from flask_cors import CORS

from .vistas.vistas_tasks import VistaTasks

app = create_app('default')
app_context = app.app_context()
app_context.push()
app.debug = True
db.init_app(app)
db.create_all()

cors = CORS(app)
api = Api(app)
api.add_resource(VistaSignIn, '/api/auth/signup')
api.add_resource(VistaLogIn, '/api/auth/login')
api.add_resource(VistaTasks, '/api/tasks')
api.add_resource(VistaTask, '/api/tasks/<int:id_task>')
api.add_resource(VistaFile, '/api/files/<string:filename>')

jwt = JWTManager(app)
