"""This file contains the route for the homepage"""


# Imports
from flask import Blueprint, render_template


# Create the Blueprint
homepage_bp: Blueprint = Blueprint(
    'homepage_bp', __name__,
    template_folder='templates',
    static_folder='static',
    static_url_path='/homepage'
)


@homepage_bp.route('/', methods=['GET'])
def homepage():
    """Method to render the homepage template"""

    return render_template('homepage.html')
