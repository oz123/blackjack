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


def test_add_card():
    assert 5 == Card('spade', 2) + Card('spade', 3)


def test_add_with_face():
    assert 13 == Card('spade', 'K') + Card('spade', 3)


def test_compare():
    assert True == (Card('spade', "Q") == Card('spade', "J"))


def test_greater_than():
    assert True == (Card('spade', "Q") > Card('spade', 3))


def test_proper_repr():

    assert "<A of spades>" == repr(Card("spade", "A"))
    assert "<A of spades>" == str(Card("spade", "A"))


def assert_truths():
    assert "A"
    assert 12
    assert [1, 1]
    assert True

    assert not None
    assert not False
    assert not []
    assert not ""


def test_init_deck():

    deck = Deck()

    assert len(deck.cards) == 52


def test_shuffle_deck():

    deck_a = Deck()
    deck_b = Deck()

    for c_a, c_b in zip(deck_a.cards, deck_b.cards):
        assert c_a.value == c_b.value

    # OK the decks are identical
    # now let's shuffle one of the decks

    deck_b.shuffle()
    randomness = []

    for c_a, c_b in zip(deck_a.cards, deck_b.cards):
        randomness.append(c_a.value != c_b.value)

    assert any(randomness)


def deal_hands():
    pass