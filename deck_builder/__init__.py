"""
This file initializes the flask app and is imported into
wsgi.py
"""


# Imports
from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from config import Config


# Create extensions objects
db: SQLAlchemy = SQLAlchemy()
login_manager: LoginManager = LoginManager()


def init_app():
    """
    Function to initialize the app object
    :returns: The app object
    """

    # Create the flask app
    app = Flask(__name__)
    app.config.from_object(Config)

    # Initialize extensions
    db.init_app(app)
    login_manager.init_app(app)

    with app.app_context():
        # Import routes
        # pylint: disable=import-outside-toplevel
        from .auth import auth_routes
        from .homepage import homepage_routes
        from .dashboard import dashboard_routes
        from .text_to_deck import text_to_deck_routes
        from .ocr import ocr_routes

        from .editor import editor_routes
        # pylint: enable=import-outside-toplevel

        # Register blueprints
        app.register_blueprint(auth_routes.auth_bp)
        app.register_blueprint(homepage_routes.homepage_bp)
        app.register_blueprint(text_to_deck_routes.text_to_deck_bp)
        app.register_blueprint(ocr_routes.ocr_bp)
        app.register_blueprint(dashboard_routes.dashboard_bp)
        app.register_blueprint(editor_routes.editor_bp)

        # Create database models
        db.create_all()

        # Return the app
        return app
