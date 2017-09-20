import pytest

from blackjack import Card, Deck


def test_card_has_suite():
    card = Card('diamond')
    assert hasattr(card, 'suit')


def test_card_has_valid_suite():

    with pytest.raises(ValueError):
        Card('robotricks')

    c = Card('spade')

    assert c.suit == 'spade'