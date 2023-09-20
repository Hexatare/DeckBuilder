"""
This file contains the class that handles creating the flashcards
"""


# Imports
import threading
from datetime import datetime
# pylint: disable=import-error
from deck_builder.models import Export, Flashcard
from deck_builder import db
# pylint: enable=import-error


class FlashcardCreator(threading.Thread):
    """
    This class adds cards to the database async using threading.Thread"""

    def __init__(self, cards: list[tuple], export_id: int, app):
        """
        Initializer
        :param list[tuple] cards: The cards generated by ChatGPT
        :param str export_id: The id of the export that the cards belong to
        :returns: None
        """

        self.__cards = cards
        self.__export_id = export_id
        self.__app = app
        super().__init__()

    def run(self) -> None:
        """Function that is run when the .start() function is called"""

        with self.__app.app_context():
            # Save the cards to the database
            for card in self.__cards:
                question, answer = card

                new_card: Flashcard = Flashcard(
                    export_id=self.__export_id,
                    front=question,
                    back=answer,
                    created_at=datetime.now()
                )

                db.session.add(new_card)

            db.session.commit()