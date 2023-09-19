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

    def __init__(self, cards: list[tuple], app):
        """
        Initializer
        :param str text: The text entered by the user
        :returns: None
        """

        self.cards = cards
        self.app = app
        super().__init__()

    def run(self) -> None:
        """Function that is run when the .start() function is called"""

        with self.app.app_context():
            # Create a new export in the database
            new_export: Export = Export(
                created_at=datetime.now()
            )

            db.session.add(new_export)
            db.session.commit()

            # Save the cards to the database
            for card in self.cards:
                question, answer = card

                new_card: Flashcard = Flashcard(
                    export_id=new_export.id,
                    front=question,
                    back=answer,
                    created_at=datetime.now()
                )

                db.session.add(new_card)

            db.session.commit()
