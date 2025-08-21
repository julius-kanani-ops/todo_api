#!/usr/bin/python3


import os


# Get the absolute path of the directory where this file is located.
base_dir = os.path.abspath(os.path.dirname(__file__))


class Config:
    SQLALCHEMY_DATABSE_URI = os.environ.get('DATABASE_URL') or\
    'sqlite:///' + os.path.join(basedir, 'tasks.db')

    SQLALCHEMY_TRACK_MODIFICATIONS = False
