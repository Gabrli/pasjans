from modules.card import Card

def test_move_card_to_foundation_wrong():
    from tests.utils.deck import deck
    deck = deck()
    deck.columns["column1"] = [Card("♠", "2", True)]
    assert deck.move_to_foundation("column1", 0) is False