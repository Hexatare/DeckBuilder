"""
This file contains route for the card editor
"""


# Imports
from flask import (
    Blueprint,
    render_template,
)
from flask_login import login_required, current_user
# pylint: disable=import-error
from deck_builder.models import Flashcard
from deck_builder import db
# pylint: enable=import-error


# Create the Blueprint
editor_bp: Blueprint = Blueprint(
    'editor_bp', __name__,
    template_folder='templates',
    static_folder='static',
    static_url_path='/editor'
)



@editor_bp.route('/editor/<int:id>', methods=['GET'])
# @login_required
def editor(id):
    """This function turns the image into text using OCR"""
    flashcards = Flashcard.query.filter_by(export_id=id).all()
    cards = [(card.front,card.back) for card in flashcards]
    return render_template("editor.html",id=id, cards=cards)
