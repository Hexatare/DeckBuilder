"""
This file contains route for the card editor
"""


# Imports
from flask import (
    Blueprint,
    render_template,
    request,
    Response
)
from flask_login import login_required, current_user
# pylint: disable=import-error
from deck_builder.models import Flashcard
from deck_builder import db
from deck_builder.text_to_deck.anki_deck_creation import gpt_to_deck
# pylint: enable=import-error


# Create the Blueprint
editor_bp: Blueprint = Blueprint(
    'editor_bp', __name__,
    template_folder='templates',
    static_folder='static',
    static_url_path='/editor'
)



@editor_bp.route('/editor/<int:id>', methods=['GET'])
@login_required
def editor(id):
    """This function returns the view of the editor"""
    flashcards = Flashcard.query.filter_by(export_id=id).all()
    cards = [(card.front,card.back) for card in flashcards]
    return render_template("editor.html",id=id, cards=cards)

@editor_bp.route('/editor/download/<int:id>', methods=['GET'])
@login_required
def editor_donwload(id):
    """This function let's you donwload your cards"""
    flashcards = Flashcard.query.filter_by(export_id=id).all()
    cards = [(card.front,card.back) for card in flashcards]
    deck = gpt_to_deck(cards)

    return Response(
        deck,
        mimetype='text/plain',
        headers={
            'Content-Disposition': 'attachment; filename=deck.txt'
        }
    )
