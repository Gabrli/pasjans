from modules.game_controller import GameController

def main():
    difficulty = input("Wybierz poziom trudności (easy/hard): ").strip().lower()
    if difficulty not in ("easy", "hard"):
        difficulty = "easy"
    GameController(difficulty).start_game()

if __name__ == "__main__":
    main()