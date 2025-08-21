#!/usr/bin/python3


from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import Config


# Initialize Extensions
db = SQLAlchemy()


def create_app(config_class=Config):
    # Create and configure the app
    app = Flask(__name__)
    app.config.from_object(config_class)

    # Initialize extensions with the app
    db.init_app(app)

    # Import the Blueprint from the routes file.
    from .routes import main as main_blueprint

    # Register the Blueprint with the flask app.
    app.register_blueprint(main_blueprint)


    return app
