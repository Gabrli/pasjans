from modules.card import Card

def test_move_card_to_foundation():
    from tests.utils.deck import deck
    deck = deck()
    deck.columns["column1"] = [Card("♠", "A", True)]
    assert deck.move_to_foundation("column1", 0) is True
    assert len(deck.finished_piles["pile1"]) == 1
    assert deck.finished_piles["pile1"][0].value == "A"