"""get_player_guess() # Pieprasa un validē ievadi (atgriež int vai None)
show_hint(result) # Parāda padomu
show_game_over(secret, attempts, won) # Beigu ziņojums
ask_play_again() # Vai spēlēt vēlreiz (atgriež bool)
"""
def get_player_guess():
    """Pieprasa un validē spēlētāja minējumu.

    Returns:
        int: Spēlētāja minējums, ja tas ir derīgs.
        None: Ja ievade nav derīga.

    Example:
        >>> get_player_guess()
        'Enter your guess: 50'
        50
    """
    try:
        guess = int(input("Enter your guess: "))
        return guess
    except ValueError:
        print("Invalid input. Please enter a number.")
        return None
    
def show_hint(result):
    """Parāda padomu atkarībā no minējuma rezultāta.

    Args:
        result (str): "correct", "too_high" vai "too_low".

    Example:
        >>> show_hint("too_low")
        'Your guess is too low.'
    """
    if result == "too_low":
        print("Your guess is too low.")
    elif result == "too_high":
        print("Your guess is too high.")
    elif result == "correct":
        print("Congratulations! You've guessed the number!")
    else:
        print("Unknown result.") 
def show_game_over(secret, attempts, won):
    """Parāda beigu ziņojumu ar slepeno skaitli un mēģinājumu skaitu.

    Args:
        secret (int): Slepenais skaitlis.
        attempts (int): Mēģinājumu skaits.
        won (bool): True, ja spēlētājs uzvarēja, False pretējā gadījumā.

    Example:
        >>> show_game_over(42, 5, True)
        'Game Over! The secret number was 42. You guessed it in 5 attempts!'
    """
    if won:
        print(f"Game Over! The secret number was {secret}. You guessed it in {attempts} attempts!")
    else:
        print(f"Game Over! The secret number was {secret}. Better luck next time!")
def ask_play_again():
    """Pajautā spēlētājam, vai viņš vēlas spēlēt vēlreiz.

    Returns:
        bool: True, ja spēlētājs vēlas spēlēt vēlreiz, False pretējā gadījumā.
    Example:
        >>> ask_play_again()
        'Do you want to play again? (y/n): y'
        True
        >>> ask_play_again()
        'Do you want to play again? (y/n): n'
        False
    """
    response = input("Do you want to play again? (y/n): ").strip().lower()
    return response == 'y'  