"""
This file contains the routes for the dashboard.
The dashboard is where users can upload an image and receive the text file
"""


# Imports
from flask import Blueprint, render_template


# Create the Blueprint
dashboard_bp: Blueprint = Blueprint(
    'dashboard_bp', __name__,
    template_folder='templates',
    static_folder='static',
    static_url_path='/dashboard'
)


@dashboard_bp.route('/dashboard', methods=['GET'])
def dashboard():
    """This route displays the dashboard"""

    return render_template('dashboard.html')
