"""
This file contains the routes for the dashboard.
The dashboard is where users can upload an image and receive the text file
"""


# Imports
from flask import Blueprint, render_template
from flask_login import login_required, current_user
from deck_builder import db
from deck_builder.models import Export


# Create the Blueprint
dashboard_bp: Blueprint = Blueprint(
    'dashboard_bp', __name__,
    template_folder='templates',
    static_folder='static',
    static_url_path='/dashboard'
)


@dashboard_bp.route('/dashboard', methods=['GET'])
@login_required
def dashboard():
    """This route displays the dashboard"""

    dates = Export.query.filter_by(user_id=current_user.id).all()
    dates = [date.created_at for date in dates]
    return render_template('dashboard.html',sessions=dates)
