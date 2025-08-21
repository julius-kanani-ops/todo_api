#!/usr/bin/python3


import os # Make sure os is imported
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app(): # We remove the config_class argument
    app = Flask(__name__)

    # Instead of loading from an object, we set the config directly
    # from the environment. This is more explicit and avoids timing issues.
    app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)

    from .routes import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app
