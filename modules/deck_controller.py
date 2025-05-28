import random
from constants.elements import VALUES, SUITS
from modules.card import Card

class Deck_Controller:
    def __init__(self, difficulty='easy'):
        self.columns = {f"column{i+1}": [] for i in range(7)}
        self.finished_piles = {f"pile{i+1}": [] for i in range(4)}
        self.reserved_cards = []
        self.draw_pile = []
        self.cards = []
        self.difficulty = difficulty
        self.reset_deck()

    def reset_deck(self):
        self.columns = {f"column{i+1}": [] for i in range(7)}
        self.finished_piles = {f"pile{i+1}": [] for i in range(4)}
        self.reserved_cards = []
        self.draw_pile = []
        self.cards = []
        self.prepare_deck()

    def prepare_deck(self):
        self.cards = [Card(suit, value) for suit in SUITS for value in VALUES]
        random.shuffle(self.cards)
        idx = 0
        for i in range(7):
            for j in range(i+1):
                card = self.cards[idx]
                card.face_up = (j == i)
                self.columns[f"column{i+1}"].append(card)
                idx += 1
        self.reserved_cards = self.cards[idx:]
  
    def reveal_last(self, column):
        if self.columns[column] and not self.columns[column][-1].face_up:
            self.columns[column][-1].face_up = True


    def draw_from_reserve(self):
        if not self.reserved_cards:
            self.reserved_cards = self.draw_pile[::-1]
            for card in self.reserved_cards:
                card.face_up = False
            self.draw_pile = []
        if self.difficulty == 'easy':
            if self.reserved_cards:
                card = self.reserved_cards.pop(0)
                card.face_up = True
                self.draw_pile = [card]
        else:  
            self.draw_pile = []
            for _ in range(3):
                if self.reserved_cards:
                    card = self.reserved_cards.pop(0)
                    card.face_up = True
                    self.draw_pile.append(card)

    def move_cards(self, from_column, to_column, count):
        if from_column not in self.columns or to_column not in self.columns:
            print(f"Nieznana kolumna. Dostępne kolumny: {list(self.columns.keys())}")
            return False
        moving = self.columns[from_column][-count:]
    
        if not moving[0].face_up:
            print("Nie można przenieść zakrytej karty.")
            return False
        if self.columns[to_column]:
            target = self.columns[to_column][-1]
            if target.face_up and moving[0].is_red() != target.is_red() and VALUES.index(moving[0].value) == VALUES.index(target.value) - 1:
                self.columns[to_column].extend(moving)
                self.columns[from_column] = self.columns[from_column][:-count]
                self.reveal_last(from_column)
                return True
            
            print("Nieprawidłowy ruch.")
            return False
        
        if moving[0].value == "K":
            self.columns[to_column].extend(moving)
            self.columns[from_column] = self.columns[from_column][:-count]
            self.reveal_last(from_column)
            return True  
        print("Tylko król może być przeniesiony na pustą kolumnę.")
        return False

    def move_to_foundation(self, from_column, pile_idx):
        pile = self.finished_piles[f"pile{pile_idx+1}"]
        if not self.columns[from_column]:
            print("Brak kart w tej kolumnie.")
            return False
        card = self.columns[from_column][-1]
        if not card.face_up:
            print("Nie można przenieść zakrytej karty.")
            return False
        if not pile:
            if card.value == "A":
                pile.append(card)
                self.columns[from_column].pop()
                self.reveal_last(from_column)
                return True
            print("Tylko as może być przeniesiony na pusty stos końcowy.")
            return False
        
        top = pile[-1]
        if card.suit == top.suit and VALUES.index(card.value) == VALUES.index(top.value) + 1:
            pile.append(card)
            self.columns[from_column].pop()
            self.reveal_last(from_column)
            return True
        print("Nieprawidłowy ruch na stos końcowy.")
        return False

    def move_draw_to_column(self, to_column):
        if not self.draw_pile:
            print("Brak kart do przeniesienia.")
            return False
        card = self.draw_pile[-1]
        if self.columns[to_column]:
            target = self.columns[to_column][-1]
            if target.face_up and card.is_red() != target.is_red() and VALUES.index(card.value) == VALUES.index(target.value) - 1:
                self.columns[to_column].append(card)
                self.draw_pile.pop()
                return True
            
            print("Nieprawidłowy ruch.")
            return False
        else:
            if card.value == "K":
                self.columns[to_column].append(card)
                self.draw_pile.pop()
                return True
       
            print("Tylko król może być przeniesiony na pustą kolumnę.")
            return False

    def is_win(self):
        return all(len(pile) == 13 for pile in self.finished_piles.values())

    def render(self):
        print("\nStosy końcowe:")
        for i, pile in enumerate(self.finished_piles.values()):
            print(f"Stos {i+1}: {pile[-1] if pile else '---'}", end="  ")
        print("\n\nKolumny:")
        max_len = max(len(col) for col in self.columns.values())
        for i in range(max_len):
            for col in self.columns.values():
                if i < len(col):
                    print(str(col[i]), end=" ")
                else:
                    print("   ", end=" ")
            print()
        print("\nStos rezerwowy:", f"{len(self.reserved_cards)} kart")
        print("Dobierane karty:", " ".join(str(card) for card in self.draw_pile))











