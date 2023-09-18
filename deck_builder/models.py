"""This file contains the database models"""


# Imports
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from . import db


class User(UserMixin, db.Model):
    """The user model"""

    # Name of table in database
    __tablename__ = 'users'

    # Id column
    id = db.Column(
        db.Integer,
        primary_key=True
    )

    # First name of the user
    first_name = db.Column(
        db.String(255),
        nullable=False
    )

    # Last name of the user
    last_name = db.Column(
        db.String(255),
        nullable=False
    )

    # Email of the user
    email = db.Column(
        db.String(255),
        nullable=False,
        unique=True
    )

    # Password of the user
    password = db.Column(
        db.String(255),
        nullable=False
    )

    def set_password(self, password: str) -> None:
        """Function to hash the password"""
        self.password = generate_password_hash(password)
    
    def check_password(self, password: str) -> bool:
        """Function to check if the password is correct"""
        return check_password_hash(self.password, password)
