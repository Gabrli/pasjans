from modules.deck_controller import Deck_Controller
from modules.card import Card

def deck():
    deck = Deck_Controller()
    deck.columns = {
        "column1": [Card("♠", "K", True)],
        "column2": [Card("♥", "Q", True)],
        "column3": [],
        "column4": [],
        "column5": [],
        "column6": [],
        "column7": []
    }
    deck.finished_piles = {f"pile{i+1}": [] for i in range(4)}
    deck.draw_pile = []
    deck.reserved_cards = []
    return deck