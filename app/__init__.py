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

    # This is a common pattern to avoid circular imports.
    # I import the routes here, after 'app' and 'db' are created.
    from app import routes, models


    return app
