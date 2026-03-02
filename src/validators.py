"""
Uzdevums 3: Validācijas bibliotēka
Mērķis: nostiprināt funkciju rakstīšanu un virkņu apstrādi; praktizēt koda organizēšanu
atsevišķā modulī.
Izveido validators.py ar funkcijām:
is_email(text) # Vienkārša e-pasta validācija (satur @ un .)
is_phone_number(text) # Latvijas formāts: +371 XXXXXXXX (8 cipari)
is_valid_age(age) # 0–150, vesels skaitlis
is_strong_password(text) # Vismaz 8 simboli, satur burtus UN ciparus
is_valid_date(text) # YYYY-MM-DD formāts (pamata pārbaude)
Prasības:
• Katra funkcija atgriež bool (True/False)
• Katra funkcija — ar docstring
• validators.py ir atsevišķs modulis: to var importēt no citiem failiem
• if __name__ == "__main__": blokā — vismaz 3 testa gadījumi katrai funkcijai
(ieskaitot robežgadījumus)
# Piemērs: validators.py palaišana atsevišķi
python validators.py
# is_email('anna@inbox.lv') → True
# is_email('anna') → False
# is_email('anna@') → False
# is_phone_number('+371 26123456') → True
# is_phone_number('26123456') → False
# ...
"""

import re

def is_email(text):
    """Pārbauda, vai teksts ir derīgs e-pasta formāts.

    Args:
        text (str): Ievades teksts.

    Returns:
        bool: True, ja teksts satur "@" un ".", pretējā gadījumā False.

    Example:
        >>> is_email("anna@inbox.lv")
        True
        >>> is_email("anna")
        False
        >>> is_email("anna@")
        False
    """
    if not isinstance(text, str):
        raise ValueError("Ievadei jābūt tekstam.")
    return "@" in text and "." in text


def is_phone_number(text):
    """Pārbauda, vai teksts atbilst Latvijas tālruņa numura formātam.

    Args:
        text (str): Ievades teksts.
    Returns:
        bool: True, ja teksts atbilst formātam +371 XXXXXXXX,
pretējā gadījumā False.
    Example:
        >>> is_phone_number("+371 26123456")
        True
        >>> is_phone_number("26123456")
        False
    """
    if not isinstance(text, str):
        raise ValueError("Ievadei jābūt tekstam.")
    pattern = r"^\+371 \d{8}$"
    return re.match(pattern, text) is not None  

def is_valid_age(age):
    """Pārbauda, vai vecums ir vesels skaitlis robežās no 0 līdz 150.

    Args:
        age (int): Vecums, ko pārbaudīt.

    Returns:
        bool: True, ja vecums ir derīgs, pretējā gadījumā False.

    Example:
        >>> is_valid_age(25)
        True
        >>> is_valid_age(-5)
        False
        >>> is_valid_age(200)
        False
    """
    if not isinstance(age, int):
        raise ValueError("Ievadei jābūt veselam skaitlim.")
    return 0 <= age <= 150  

def is_strong_password(text):
    """Pārbauda, vai parole ir stipra (vismaz 8 simboli, satur burtus un ciparus).

    Args:
        text (str): Parole, ko pārbaudīt.
    Returns:
        bool: True, ja parole ir stipra, pretējā gadījumā False.
    Example:
        >>> is_strong_password("Passw0rd")
        True
        >>> is_strong_password("password")
        False    
        >>> is_strong_password("12345678")
        False
    """
    if not isinstance(text, str):
        raise ValueError("Ievadei jābūt tekstam.")
    has_letter = any(c.isalpha() for c in text)
    has_digit = any(c.isdigit() for c in text)
    return len(text) >= 8 and has_letter and has_digit

def is_valid_date(text):
    """Pārbauda, vai teksts atbilst datuma formātam YYYY-MM-DD.

    Args:
        text (str): Ievades teksts.
    Returns:
        bool: True, ja teksts atbilst formātam, pretējā gadījumā False.
    Example:
        >>> is_valid_date("2024-06-15")
        True
        >>> is_valid_date("15-06-2024")
        False
        >>> is_valid_date("2024/06/15")
        False
    """
    if not isinstance(text, str):
        raise ValueError("Ievadei jābūt tekstam.")
    pattern = r"^\d{4}-\d{2}-\d{2}$"
    return re.match(pattern, text) is not None

if __name__ == "__main__":
    # Testa gadījumi is_email funkcijai
    print(is_email("anna@inbox.lv"))  # True
    print(is_email("anna"))  # False
    print(is_email("anna@"))  # False
    # Testa gadījumi is_phone_number funkcijai
    print(is_phone_number("+371 26123456"))  # True
    print(is_phone_number("26123456"))  # False
    # Testa gadījumi is_valid_age funkcijai
    print(is_valid_age(25))  # True
    print(is_valid_age(-5))  # False
    print(is_valid_age(200))  # False
    # Testa gadījumi is_strong_password funkcijai
    print(is_strong_password("Passw0rd"))  # True
    print(is_strong_password("password"))  # False    
    print(is_strong_password("12345678"))  # False
    # Testa gadījumi is_valid_date funkcijai
    print(is_valid_date("2024-06-15"))  # True
    print(is_valid_date("15-06-2024"))  # False
    print(is_valid_date("2024/06/15"))  # False