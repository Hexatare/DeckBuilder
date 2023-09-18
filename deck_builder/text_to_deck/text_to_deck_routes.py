"""This file contains the route for the text to deck"""

from flask import Blueprint, jsonify


# Create the Blueprint
text_to_deck_bp: Blueprint = Blueprint(
    'text_to_deck_bp', __name__,
    template_folder='templates',
    static_folder='static',
    static_url_path='/text_to_deck'
)


"""
This endpoint gets a text from which it generates Anki flashcards
"""
@text_to_deck_bp.route('/upload/text', methods=['POST'])
def text_to_deck():
    data = request.get_json()
    text = data["text"]
    # text to cards
    # cards to deck
    deck = "front of card; back of card"
    return jsonify(file_contents=deck)
    
