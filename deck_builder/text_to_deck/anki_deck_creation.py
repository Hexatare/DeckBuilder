import unittest
import re


def gpt_to_deck(cards):
    """
    This function gives back a string which represents an Anki deck in textfile format.
    https://docs.ankiweb.net/importing/text-files.html

    Args:
        cards (list of tuples): A list of tuples where each tuple contains to strings representing the front and the back of the card respectively. 

    Returns:
        str: Anki deck string

    Raises:
        ValueError: If cards don't match the expected format.
    """
    cards_as_deck = []

    try:
        iter(cards)
    except:
        raise ValueError
    
    for card in cards:
        if len(card) != 2:
            raise ValueError
        if type(card[0]) != str or type(card[1]) != str:
            raise ValueError

        front = card[0].replace('"','""')
        back = card[1].replace('"','""')
        front = f'"{front}"'
        back = f'"{back}"'
        cards_as_deck.append(f'{front};{back}')
    return '\n'.join(cards_as_deck)
 
       
class TestCalculations(unittest.TestCase):
    pattern = r'^"([^"]|"")*";"([^"]|"")*"$'

    def test_semicolon(self):
        deck = gpt_to_deck([('front;of card','back ;of card')])
        self.assertTrue(re.match(self.pattern,deck))

    def test_doublequote(self):
        deck = gpt_to_deck([('front " of the card "','back of " the card " ')])
        self.assertTrue(re.match(self.pattern,deck))

    def test_valurerrortupletolong(self):
        with self.assertRaises(ValueError):
            gpt_to_deck([('','','')])
            
    def test_valurerrornoiterable(self):
        with self.assertRaises(ValueError):
            gpt_to_deck(1)

if __name__ == '__main__':
    unittest.main()
