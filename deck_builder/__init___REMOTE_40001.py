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
        from .homepage import homepage_routes
        from .auth import auth_routes
        from .dashboard import dashboard_routes
        # pylint: enable=import-outside-toplevel

        # Register blueprints
        app.register_blueprint(auth_routes.auth_bp)
        app.register_blueprint(homepage_routes.homepage_bp)
        app.register_blueprint(dashboard_routes.dashboard_bp)

        # Create database models
        db.create_all()

        # Return the app
        return app