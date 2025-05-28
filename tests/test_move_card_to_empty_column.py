def test_move_card_to_empty_column():
    from tests.utils.deck import deck
    deck = deck()
    assert deck.move_cards("column1", "column3", 1) is True
    assert len(deck.columns["column1"]) == 0
    assert len(deck.columns["column3"]) == 1
    assert deck.columns["column3"][0].value == "K"

