"""
This file contains the routes for the create deck page
"""


# Imports
import base64
from flask import (
    Blueprint,
    render_template,
    request,
    jsonify,
    current_app as app
)
# pylint: disable=import-error
from deck_builder.flashcard_creator.flashcard_creator import FlashcardCreator
from deck_builder.text_to_deck.chatgpt_api import prompt_chatgpt
from deck_builder.ocr import ocr
# pylint: enable=import-error


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


@create_deck_bp.route('/create/upload/text', methods=['POST'])
def upload_text():
    """This function handles the uploaded text"""

    # Get the text
    data: dict = request.get_json()
    text: str = data["text"]

    # Prompt ChatGPT
    success, cards = prompt_chatgpt(text)

    if not success:
        return jsonify(error=cards), 500

    # Create a new flashcard creator and start it
    FlashcardCreator(cards, app._get_current_object()).start() # pylint: disable=protected-access

    return jsonify(success=True), 200


@create_deck_bp.route('/create/upload/image', methods=['POST'])
def upload_image():
    """This function turns the image into text using OCR"""

    # Get the image
    image = request.files.get('image', '')

    if not image:
        return jsonify(error='no_image'), 500

    # Read the contents of the uploaded image file and convert it to base64
    image_data = image.read()
    base64_encoded_image = base64.b64encode(image_data).decode('utf-8')

    # Get the text using the image_to_text function
    text: str = ocr.image_to_text(base64_encoded_image)

    return jsonify(text=text), 200
