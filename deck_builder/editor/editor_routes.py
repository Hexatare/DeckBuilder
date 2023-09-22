"""
This file contains route for the card editor
"""


# Imports
from flask import (
    Blueprint,
    render_template,
    request,
    Response,
    jsonify
)
from flask_login import login_required, current_user
# pylint: disable=import-error
from deck_builder.models import Flashcard, Export
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
    
    if Export.query.filter_by(id=id).all()[0].user_id != current_user.id:
        return render_template("no.html")
        
    flashcards = Flashcard.query.filter_by(export_id=id).all()
    cards = [(card.front.strip(),card.back.strip(),card.id) for card in flashcards]
    return render_template("editor.html",id=id, cards=cards)

@editor_bp.route('/editor/download/<int:id>', methods=['GET'])
@login_required
def editor_donwload(id):
    """This function let's you donwload your cards"""

    if Export.query.filter_by(id=id).all()[0].user_id != current_user.id:
        return render_template("no.html")

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

@editor_bp.route('/editor/save', methods=['POST'])
@login_required
def editor_update_card():
    """This function updates a card"""
    
    data: dict = request.get_json()
    data = data["cards"]
    for card in data:
        flashcard = Flashcard.query.get(card["id"])
        
        export_id = flashcard.export_id
        if Export.query.filter_by(id=export_id).all()[0].user_id != current_user.id:
            return render_template("no.html")
        
        flashcard.front = card["front"]
        flashcard.back = card["back"]
    db.session.commit()
    return jsonify({'message': 'Flashcard updated successfully'}), 200

@editor_bp.route('/editor/remove/<int:card_id>', methods=['POST'])
@login_required
def editor_remove_card(card_id):
    """This function removes a card"""
    flashcard = Flashcard.query.get(card_id)

    export_id = flashcard.export_id
    if Export.query.filter_by(id=export_id).all()[0].user_id != current_user.id:
        return render_template("no.html")

    db.session.delete(flashcard)
    db.session.commit()
    return jsonify({'message': 'Flashcard removed successfully'}), 200
