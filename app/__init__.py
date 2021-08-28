# app/__init__

import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_bootstrap import Bootstrap
from flask_login import LoginManager

db = SQLAlchemy()
bcrypt = Bcrypt()

login_manager = LoginManager()
# Letting login manager know where the Login Route exists
login_manager.login_view = 'authentication.login_the_user'
login_manager.session_protection = 'strong'

bootstrap = Bootstrap()

def create_app(config_type): # dev, test, prod
    app = Flask(__name__)
    configuration = os.path.join(os.getcwd(), 'config', config_type + '.py')

    app.config.from_pyfile(configuration)  # Flask configuration variables
    db.init_app(app) # initialize db by passing app
    bcrypt.init_app(app)
    bootstrap.init_app(app)
    login_manager.init_app(app)

    from app.catalog import main
    app.register_blueprint(main) # Register blueprint

    from app.auth import authentication
    app.register_blueprint(authentication)

    return app
