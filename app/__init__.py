from flask import Flask
from app.extensions import ma,db,mi,jwt
from .config import Config

from app.users.routes import user_api
from app.medicine.routes import medicine_api
from app.checklist.routes import checklist_api



def create_app():
    app = Flask(__name__)

    app.config.from_object(Config)

    ma.init_app(app)
    db.init_app(app)
    mi.init_app(app, db)
    jwt.init_app(app)
    
    app.register_blueprint(user_api)
    app.register_blueprint(medicine_api)
    app.register_blueprint(checklist_api)

    return app