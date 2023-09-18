"""Flask app config"""


# Imports
from os import environ, path
from dotenv import load_dotenv


# Load enviroment variables from the .env file
basedir = path.abspath(path.dirname(__file__))
load_dotenv(path.join(basedir, '.env'))


# pylint: disable=too-few-public-methods
class Config:
    """Config class for the Flask app"""

    # Set Flask configuration from environment variables
    FLASK_APP = 'wsgi.py'
    FLASK_ENV = environ.get('FLASK_ENV')
    SECRET_KEY = environ.get('SECRET_KEY')
    SERVER_NAME = environ.get('SERVER_NAME')
    DEBUG = environ.get('DEBUG')

    # Static Assets
    STATIC_FOLDER = 'static'
    TEMPLATES_FOLDER = 'templates'

    # Flask-SQLAlchemy
    SQLALCHEMY_DATABASE_URI = environ.get('SQLALCHEMY_DATABASE_URI')
    SQLALCHEMY_ECHO = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # Flask-Session
    SESSION_COOKIE_DOMAIN = environ.get('SESSION_COOKIE_DOMAIN')

    # Root directory of project
    PROJECT_ROOT = environ.get('PROJECT_ROOT')
