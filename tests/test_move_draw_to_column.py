from modules.card import Card

def test_move_draw_to_column():
    from tests.utils.deck import deck
    deck = deck()
    deck.draw_pile = [Card("♣", "K", True)]
    assert deck.move_draw_to_column("column3") is True
    assert len(deck.columns["column3"]) == 1
    assert deck.columns["column3"][0].value == "K"