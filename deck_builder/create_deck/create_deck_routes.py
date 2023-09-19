"""
This file contains the routes for the create deck page
"""


# Imports
from flask import Blueprint, render_template


# Create the Blueprint
create_deck_bp: Blueprint = Blueprint(
    'create_deck_bp', __name__,
    template_folder='templates',
    static_folder='static',
    static_url_path='/create_deck'
)


@create_deck_bp.route('/create', methods=['GET'])
def create_deck():
    """This function renders the template for the create deck route"""

    return render_template('create_deck.html')
