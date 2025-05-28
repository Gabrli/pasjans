
## Spis treści
- [Opis projektu](#opis-projektu)
- [Sposób uruchomienia](#sposób-uruchomienia)
- [Instrukcja rozgrywki](#instrukcja-rozgrywki)
- [Struktura projektu i opis modułów](#struktura-projektu-i-opis-modułów)
- [Opis klas i metod](#opis-klas-i-metod)
- [Testy jednostkowe](#testy-jednostkowe)

---

## Opis projektu

Celem gry jest ułożenie wszystkich kart na czterech stosach końcowych według koloru i rosnącej wartości (od Asa do Króla). Gra posiada dwa poziomy trudności (łatwy i trudny), obsługę cofania ruchów oraz ranking wyników.

---

## Sposób uruchomienia

1. **Wymagania:**
   - Python 3.10 lub nowszy
   - (Opcjonalnie) pytest do uruchamiania testów jednostkowych

2. **Kroki:**
   1. Sklonuj lub pobierz repozytorium do wybranego katalogu.
   2. Przejdź do katalogu głównego projektu w terminalu:
      ```
      cd ścieżka/do/projektu
      ```
   3. Uruchom grę poleceniem:
      ```
      python main.py
      ```
   4. (Opcjonalnie) Aby uruchomić testy jednostkowe:
      ```
      pytest
      ```

---

## Instrukcja rozgrywki

- Po uruchomieniu gry wybierz poziom trudności: `easy` (dobieranie po 1 karcie) lub `hard` (dobieranie po 3 karty, użyć można tylko wierzchniej).
- Gra wyświetli aktualny układ kart: kolumny, stosy końcowe, stos rezerwowy i dobierane karty.
- Dostępne komendy (wpisuj w konsoli):

  - `move <from_col> <to_col> <count>`  
    Przenieś sekwencję kart z jednej kolumny do drugiej.  
    Przykład: `move column2 column3 2`

  - `draw`  
    Dobierz kartę/karty ze stosu rezerwowego.

  - `movef <from_col> <pile>`  
    Przenieś kartę z kolumny na stos końcowy.  
    Przykład: `movef column1 1`

  - `drawcol <to_col>`  
    Przenieś kartę z dobieranych do wybranej kolumny.  
    Przykład: `drawcol column4`

  - `undo`  
    Cofnij ostatni ruch (możesz cofnąć do 3 ruchów).

  - `restart`  
    Rozpocznij nową grę.

  - `quit`  
    Zakończ grę.

- Po wygranej gra zapisze Twój wynik (liczbę ruchów) do pliku `ranking.txt`.

---

## Struktura projektu i opis modułów

```
pasjans/
│
├── main.py                  # Główny plik uruchamiający grę
├── modules/
│   ├── card.py              # Klasa reprezentująca pojedynczą kartę
│   ├── deck_controller.py   # Logika talii, kolumn, stosów i ruchów
│   └── game_controller.py   # Obsługa rozgrywki i interfejsu tekstowego
├── constants/
│   ├── elements.py          # Stałe: kolory i wartości kart
│   └── colors.py            # Stałe: kody kolorów ANSI do wyświetlania kart
├── tests/
│   ├── test_*.py            # Testy jednostkowe (pytest)
│   └── utils/
│       └── deck.py          # Pomocnicze funkcje do testów
└── ranking.txt              # Plik z wynikami graczy
```

---

## Opis klas i metod

### `modules/card.py`
- **Card**  
  Reprezentuje pojedynczą kartę.  
  - `suit` – kolor (♥, ♦, ♠, ♣)
  - `value` – wartość (A, 2, ..., K)
  - `face_up` – czy karta jest odkryta
  - `__str__()` – zwraca reprezentację tekstową karty z kolorem
  - `is_red()` / `is_black()` – sprawdza kolor karty

### `modules/deck_controller.py`
- **Deck_Controller**  
  Zarządza talią, kolumnami, stosami końcowymi i ruchem kart.
  - `reset_deck()` – resetuje i rozkłada karty
  - `prepare_deck()` – przygotowuje nową talię i rozkłada karty na kolumny
  - `draw_from_reserve()` – dobiera kartę/karty ze stosu rezerwowego
  - `move_cards(from_col, to_col, count)` – przenosi sekwencję kart między kolumnami
  - `move_to_foundation(from_col, pile_idx)` – przenosi kartę na stos końcowy
  - `move_draw_to_column(to_col)` – przenosi kartę z dobieranych do kolumny
  - `is_win()` – sprawdza, czy gra została wygrana
  - `render()` – wyświetla aktualny stan gry

### `modules/game_controller.py`
- **GameController**  
  Obsługuje pętlę gry, przyjmuje komendy użytkownika, zarządza cofaniem ruchów i rankingiem.
  - `start_game()` – główna pętla gry
  - `save_state()` – zapisuje stan gry do cofania
  - `undo()` – cofa ostatni ruch
  - `save_score()` – zapisuje wynik do rankingu

### `constants/elements.py`
- Stałe: `SUITS` (kolory), `VALUES` (wartości kart)

### `constants/colors.py`
- Stałe: `RED`, `BLACK`, `RESET` – kody kolorów ANSI

---

## Testy jednostkowe

Testy znajdują się w katalogu `tests/`.  
Aby uruchomić testy:
```
pytest
```
Testy sprawdzają m.in. poprawność przenoszenia kart, ruchów na stosy końcowe, dobierania kart i nieprawidłowych ruchów.

