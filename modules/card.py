from constants.colors import RED, BLACK, RESET

class Card:
    def __init__(self, suit, value, face_up=False):
        self.suit = suit
        self.value = value
        self.face_up = face_up
        self.color = RED if suit in ["♥", "♦"] else BLACK

    def __str__(self):
        if not self.face_up:
            return "🂠"
        return f"{self.color}{self.value}{self.suit}{RESET}"

    def is_red(self):
        return self.suit in ["♥", "♦"]

    def is_black(self):
        return self.suit in ["♠", "♣"]
