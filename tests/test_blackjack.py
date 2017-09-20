from blackjack import Card, Deck


def test_card_has_suite():
    card = Card('diamond')
    assert hasattr(card, 'suit')