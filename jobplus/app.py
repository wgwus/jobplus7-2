from flask import Flask
from flask_migrate import Migrate
from jobplus.config import configs
from jobplus.models import db 
from flask_login import LoginManager

def register_extensions(app):
    db.init_app(app)    # No test 
    Migrate(app, db)    # No test
    # LoginManager = LoginManager
    # login_manager.init_app(app)

    #user and company need to login


def register_blueprints(app):
    from .handlers import front
    app.register_blueprint(front)

def create_app(config):
    app = Flask(__name__)
    app.config.from_object(configs.get(config))

    register_extensions(app)
    register_blueprints(app)

    return app
