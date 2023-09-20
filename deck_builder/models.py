"""This file contains the database models"""
# pylint: disable=too-few-public-methods

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


class Export(db.Model):
    """The model for an export"""

    # Name of the table in the database
    __tablename__ = 'exports'

    # Id column
    id = db.Column(
        db.Integer,
        primary_key=True
    )

    # User ID
    user_id = db.Column(
        db.Integer,
        db.ForeignKey('users.id')
        nullable=False
    )
    
    # When the export was created
    created_at = db.Column(
        db.DateTime,
        nullable=False
    )



class Flashcard(db.Model):
    """The model for a flashcard"""

    # Name of the table in the database
    __tablename__ = 'flashcards'

    # Id column
    id = db.Column(
        db.Integer,
        primary_key=True
    )

    # The export the card is from
    export_id = db.Column(
        db.Integer,
        db.ForeignKey('exports.id'),
        nullable=False
    )

    front = db.Column(
        db.String(255),
        nullable=False,
        default=''
    )

    back = db.Column(
        db.String(255),
        nullable=False,
        default=''
    )

    # When the flashcard was created
    created_at = db.Column(
        db.DateTime,
        nullable=False
    )

