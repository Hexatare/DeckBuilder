"""
This file contains the routes for the create deck page
"""


# Imports
import base64
from datetime import datetime
from flask import (
    Blueprint,
    render_template,
    request,
    jsonify,
    redirect,
    url_for,
    current_app as app
)
# pylint: disable=import-error
from flask_login import login_required, current_user
from deck_builder.flashcard_creator.flashcard_creator import FlashcardCreator
from deck_builder.text_to_deck.chatgpt_api import prompt_chatgpt
from deck_builder.ocr import ocr
from deck_builder.models import Export
from deck_builder import db
# pylint: enable=import-error


# Create the Blueprint
create_deck_bp: Blueprint = Blueprint(
    'create_deck_bp', __name__,
    template_folder='templates',
    static_folder='static',
    static_url_path='/create_deck'
)


@create_deck_bp.route('/create', methods=['GET'])
@login_required
def create_deck():
    """This function renders the template for the create deck route"""

    return render_template('create_deck.html')


@create_deck_bp.route('/create/upload/text', methods=['POST'])
@login_required
def upload_text():
    """This function handles the uploaded text"""

    # Get the text
    data: dict = request.get_json()
    text: str = data["text"]

    # Prompt ChatGPT
    success, cards = prompt_chatgpt(text)

    if not success:
        return jsonify(error=cards), 500

    # Create a new export
    new_export: Export = Export(
        created_at=datetime.now(),
        user_id = current_user.id
    )

    db.session.add(new_export)
    db.session.commit()

    # Create a new flashcard creator and start it
    FlashcardCreator(cards, new_export.id, app._get_current_object()).start() # pylint: disable=protected-access

    return redirect(url_for('editor_bp.editor',id=new_export.id))


@create_deck_bp.route('/create/upload/image', methods=['POST'])
@login_required
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
