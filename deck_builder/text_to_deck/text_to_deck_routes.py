"""This file contains the route for the text to deck"""

from flask import Blueprint, jsonify, request
from .anki_deck_creation import gpt_to_deck
from .chatgpt_api import get_list


# Create the Blueprint
text_to_deck_bp: Blueprint = Blueprint(
    "text_to_deck_bp",
    __name__,
    template_folder="templates",
    static_folder="static",
    static_url_path="/text_to_deck",
)


@text_to_deck_bp.route("/upload/text", methods=["POST"])
def text_to_deck():
    """
    This endpoint gets a text from which it generates Anki flashcards
    """
    # Get the text
    data: dict = request.get_json()
    text: str = data["text"]

    # Get the cards
    status: str
    cards: list[tuple] | str
    status, cards = get_list(text)

    # Check if generating the cards was succesful
    if status == "success":
        # Get the deck using the gpt_to_deck() function
        deck: str = gpt_to_deck(cards)
        
        return jsonify(file_contents=deck), 200
    
    return jsonify(cards=cards), 200
