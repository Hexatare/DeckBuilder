"""
This file contains the routes for the editor
"""


# Imports
from flask import Blueprint, render_template


# Create the Blueprint
editor_bp: Blueprint = Blueprint(
    'editor_bp', __name__,
    template_folder='templates',
    static_folder='static',
    static_url_path='/editor'
)


@editor_bp.route('/edit', methods=['GET'])
def editor():
    """This function renders the template for the editor route"""

    return render_template('editor.html')
