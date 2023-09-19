"""This file handles the image to text conversion"""


# Imports
from flask import Blueprint, request, jsonify

# pylint: disable=no-name-in-module
from . import ocr


# Create the Blueprint
ocr_bp: Blueprint = Blueprint(
    "ocr_bp",
    __name__,
    template_folder="templates",
    static_folder="static",
    static_url_path="/ocr",
)


@ocr_bp.route("/upload/image", methods=["POST"])
def ocr_endpoint():
    """
    This endpoint gets an image from which it extracts the text
    """
    data = request.get_json()
    image = data["image"]
    text = ocr.image_to_text(image)
    return jsonify(text), 200
