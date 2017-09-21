import pytest

from blackjack import Card, Deck


def test_card_has_suite():
    card = Card('diamond', 2)
    assert hasattr(card, 'suit')


def test_card_has_valid_suite():

    with pytest.raises(ValueError):
        Card('robotricks', 2)

    c = Card('spade', 2)

    assert c.suit == 'spade'


def test_card_has_a_value():
    king_of_spades = Card('spade', 'K')
    queen_of_spades = Card('spade', 'Q')

    assert king_of_spades.value == 'K'
    assert king_of_spades.value != 'Q'