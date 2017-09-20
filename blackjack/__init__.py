
class Card:

    def __init__(self, suit):

        if suit not in ['spade', 'club', 'diamond', 'heart']:
            raise ValueError(
                "{} must be in ['spade', 'club', 'diamond', 'heart']")

        self.suit = suit


class Deck:
    pass