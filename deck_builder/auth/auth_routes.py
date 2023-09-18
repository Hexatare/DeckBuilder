"""This file handles the user authentication"""


# Imports
from flask import redirect, url_for, Blueprint
# pylint: disable=import-error
from deck_builder.models import User
from deck_builder import login_manager, db
# pylint: enable=import-error


# Create the Blueprint
auth_bp: Blueprint = Blueprint(
    'auth_bp', __name__,
    template_folder='templates',
    static_folder='static',
    static_url_path='/auth'
)


@login_manager.user_loader
def load_user(user_id: int) -> User:
    """
    The user loader
    :param int user_id: The id of the user
    """

    # Check if user is logged-in on every page load.
    if user_id:
        return db.session.query(User).get(user_id)
    return None


@login_manager.unauthorized_handler
def unauthorized():
    """The unauthorized handler"""

    # Redirect unauthorized users to Login page.
    return redirect(url_for('auth_bp.login'))
