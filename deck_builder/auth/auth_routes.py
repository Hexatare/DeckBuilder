"""This file handles the user authentication"""


# Imports
from datetime import datetime
from flask import (
    redirect,
    url_for,
    Blueprint,
    render_template,
    request,
    jsonify
)
from flask_login import login_user, current_user, login_required, logout_user
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


@auth_bp.route('/login', methods=['GET'])
def login():
    """This route displays the login page"""

    # Check if the user is already logged in
    if current_user.is_authenticated:
        return redirect(url_for('dashboard_bp.dashboard'))

    return render_template('login.html')


@auth_bp.route('/login/submit', methods=['POST'])
def submit_login():
    """This route handles the user clicking the "login" button"""

    # Get the email and password
    data: dict = request.get_json()
    email: str = data['email']
    password: str = data['password']

    user: User = db.session.query(User).filter_by(email=email).first()

    if user and user.check_password(password):
        # Set the "last login" to now
        user.last_login = datetime.now()
        db.session.commit()

        login_user(user)

        return redirect(url_for('dashboard_bp.dashboard'))
    
    return jsonify(success=False), 401


@auth_bp.route('/signup', methods=['GET'])
def signup():
    """This route renders the template for the sign up page"""

    # Check if the user is already logged in
    if current_user.is_authenticated:
        return redirect(url_for('dashboard_bp.dashboard'))

    return render_template('signup.html')


@auth_bp.route('/signup/submit', methods=['POST'])
def submit_signup():
    """This route creates a new user account"""

    # Get the data
    data: dict = request.get_json()
    first_name: str = data['first_name']
    last_name: str = data['last_name']
    email: str = data['email']
    password: str = data['password']

    # Check if an account already exists with that email
    if db.session.query(User).filter_by(email=email).first():
        return jsonify(error=user_exists), 500

    # Create the user and set the password
    new_user: User = User(
        first_name=first_name,
        last_name=last_name,
        email=email,
        last_login=datetime.now(),
        created_at=datetime.now()
    )

    new_user.set_password(password)

    # Add the user to the db
    db.session.add(new_user)
    db.session.commit()

    # Log the user in a redirect
    login_user(new_user)

    return redirect(url_for('dashboard_bp.dashboard'))


@auth_bp.route('/logout', methods=['GET'])
@login_required
def logout():
    logout_user()

    return redirect(url_for('auth_bp.login'))


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
