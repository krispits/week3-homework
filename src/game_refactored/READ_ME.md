Uzdevums 4: Minēšanas spēles refaktorings — modulāra struktūra
Mērķis: apgūt koda sadalīšanu vairākos failos (import), refaktoringu un projekta struktūru.
Pārveido 2. nedēļas guess.py modulārā struktūrā ar vismaz 3 failiem:
game_refactored/
├── game_logic.py # Spēles loģikas funkcijas
├── ui.py # Ievades/izvades funkcijas
├── main.py # Galvenais ieejas punkts
└── validators.py # Var importēt no 3. uzdevuma!
game_logic.py satur:
generate_secret(low=1, high=100) # Ģenerē nejaušu skaitli
check_guess(guess, secret) # Atgriež "correct", "too_high" vai "too_low"
is_game_over(attempts, max_attempts=10) # Vai spēle beigusies
ui.py satur:
get_player_guess() # Pieprasa un validē ievadi (atgriež int vai None)
show_hint(result) # Parāda padomu
show_game_over(secret, attempts, won) # Beigu ziņojums
ask_play_again() # Vai spēlēt vēlreiz
main.py:
from game_logic import generate_secret, check_guess, is_game_over
from ui import get_player_guess, show_hint, show_game_over, ask_play_again
def play_round():
"""Viena spēles raunda loģika."""
secret = generate_secret()
attempts = 0
while not is_game_over(attempts):
guess = get_player_guess()
if guess is None:
continue
attempts += 1
result = check_guess(guess, secret)
if result == "correct":
show_game_over(secret, attempts, won=True)
return
show_hint(result)
show_game_over(secret, attempts, won=False)
if __name__ == "__main__":
while True:
play_round()
if not ask_play_again():
break