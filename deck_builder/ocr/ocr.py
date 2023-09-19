"""Module providing a function image_to_text using keras-ocr"""

import string
import base64
import io
import keras_ocr
from PIL import Image


# keras-ocr will automatically download pretrained
# weights for the detector and recognizer.
pipeline = keras_ocr.pipeline.Pipeline(
    recognizer=keras_ocr.recognition.Recognizer(
        alphabet=string.digits + string.ascii_lowercase
    )
)


def image_to_text(img: str) -> str:
    """
    Convert an image to text.

        Args:
            img: A base-64 encoded image
    """

    base64_decoded = base64.b64decode(img)

    Image.open(io.BytesIO(base64_decoded)).save("image.png")

    image = keras_ocr.tools.read("image.png")

    # words consists of (word, box) tuples.
    words = pipeline.recognize([image])[0]

    # Sorting the words
    words.sort(key=lambda word: word[1][0][1])

    lines = []
    while len(words):
        lines.append([])
        max_line_y = words[0][1][3][1]
        while len(words):
            if words[0][1][0][1] > max_line_y:
                break
            lines[-1].append(words.pop(0))
        lines[-1].sort(key=lambda word: word[1][0][0])

    return " ".join([" ".join([word[0] for word in line]) for line in lines])

