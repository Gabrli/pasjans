from modules.card import Card

def test_move_card_wrong_color():
    from tests.utils.deck import deck
    deck = deck()
    deck.columns["column3"] = [Card("♠", "K", True)]
    assert deck.move_cards("column2", "column3", 1) is True  
    deck.columns["column4"] = [Card("♥", "J", True)]
    assert deck.move_cards("column3", "column4", 1) is False  

