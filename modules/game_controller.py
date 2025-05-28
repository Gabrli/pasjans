import copy
from modules.deck_controller import Deck_Controller

class GameController:
    def __init__(self, difficulty='easy'):
        self.deck = Deck_Controller(difficulty)
        self.moves = 0
        self.undo_stack = []

    def start_game(self):
        while True:
            self.deck.render()
            print(f"\nLiczba ruchów: {self.moves}")
            print("Komendy: move <from_col> <to_col> <count>, draw, movef <from_col> <pile>, drawcol <to_col>, undo, restart, quit")
            print(f"Dostępne kolumny: {', '.join(self.deck.columns.keys())}")
            cmd = input("Twój ruch: ").strip().split()
            if not cmd:
                continue
            if cmd[0] == "move" and len(cmd) == 4:
                self.save_state()
                if self.deck.move_cards(cmd[1], cmd[2], int(cmd[3])):
                    self.moves += 1
            if cmd[0] == "draw":
                self.save_state()
                self.deck.draw_from_reserve()
                self.moves += 1
            if cmd[0] == "movef" and len(cmd) == 3:
                self.save_state()
                if self.deck.move_to_foundation(cmd[1], int(cmd[2])-1):
                    self.moves += 1
            if cmd[0] == "drawcol" and len(cmd) == 2:
                self.save_state()
                if self.deck.move_draw_to_column(cmd[1]):
                    self.moves += 1
            if cmd[0] == "undo":
                self.undo()
            if cmd[0] == "restart":
                self.deck.reset_deck()
                self.moves = 0
                self.undo_stack = []
            if cmd[0] == "quit":
                print("Koniec gry.")
                break
            else:
                print("Nieznana komenda.")
            if self.deck.is_win():
                print("Gratulacje! Wygrałeś pasjansa!")
                self.save_score()
                break

    def save_state(self):
        if len(self.undo_stack) >= 3:
            self.undo_stack.pop(0)
        self.undo_stack.append((copy.deepcopy(self.deck), self.moves))

    def undo(self):
        if self.undo_stack:
            self.deck, self.moves = self.undo_stack.pop()
            print("Cofnięto ruch.")
        else:
            print("Brak ruchów do cofnięcia.")

    def save_score(self):
        try:
            with open("ranking.txt", "a") as f:
                f.write(f"{self.moves}\n")
            print("Wynik zapisany do rankingu.")
        except Exception as e:
            print(f"Błąd zapisu rankingu: {e}")