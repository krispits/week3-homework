
#def generate_secret(low=1, high=100) # Ģenerē nejaušu skaitli
#def check_guess(guess, secret) # Atgriež "correct", "too_high" vai "too_low"
#def is_game_over(attempts, max_attempts=10) # Vai spēle beigusies"""

def generate_secret(low=1, high=100):
    """Ģenerē nejaušu skaitli norādītajā diapazonā.

    Args:
        low (int): Diapazona apakšējā robeža (iekļauta).
        high (int): Diapazona augšējā robeža (iekļauta).

    Returns:
        int: Ģenerētais nejaušais skaitlis.

    Example:
        >>> generate_secret(1, 10)
        7
    """
    import random
    return random.randint(low, high)

def check_guess(guess, secret):
    """Pārbauda, vai minējums ir pareizs, par augstu vai par zemu.

    Args:
        guess (int): Spēlētāja minējums.
        secret (int): Slepenais skaitlis.
    Returns:
        str: "correct", "too_high" vai "too_low" atkarībā no minējuma.
    Example:
        >>> check_guess(5, 7)
        'too_low'
        >>> check_guess(9, 7)
        'too_high'
        >>> check_guess(7, 7)
        'correct'
    """
    if guess < secret:
        return "too_low"
    elif guess > secret:
        return "too_high"
    else:
        return "correct"
    
def is_game_over(attempts, max_attempts=10):
    """Pārbauda, vai spēle ir beigusies pēc noteikta mēģinājumu skaita.

    Args:
        attempts (int): Pašreizējais mēģinājumu skaits.
        max_attempts (int): Maksimālais mēģinājumu skaits.
    Returns:
        bool: True, ja mēģinājumu skaits ir sasniedzis maksimālo, pretējā gadījumā False.
    Example:
        >>> is_game_over(5, 10)
        False
        >>> is_game_over(10, 10)
        True
    """
    return attempts >= max_attempts