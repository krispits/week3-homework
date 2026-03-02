"""Uzdevums 2: Utilītu bibliotēka
Mērķis: apgūt def, parametrus, return, noklusējuma vērtības un docstring; izveidot atkārtoti
lietojamu kodu.
Izveido utils.py ar vismaz 8 funkcijām:
Virkņu funkcijas:
capitalize(text) # "hello" → "Hello"
truncate(text, max_len=20) # Apgriež un pievieno "..."
count_words(text) # Saskaita vārdus
Skaitļu funkcijas:
clamp(num, low, high) # Ierobežo/pārveido vērtību diapazonā
is_prime(num) # Vai ir pirmskaitlis (atgriež bool)
factorial(n) # n! (ar validāciju: n >= 0)
Sarakstu funkcijas:
total(numbers) # Saraksta summa (ar for, ne sum())
average(numbers) # Vidējais aritmētiskais
Prasības:
• Katrai funkcijai — docstring ar aprakstu, parametriem, atgriežamo vērtību un piemēru
• Vismaz 2 funkcijām — noklusējuma parametru vērtības
• Funkcijas ir "tīras" (pure): nav blakusefektu, nav print() iekšpusē (izņemot
demonstrācijai)
• Katra funkcija validē ievadi: piem., factorial(-1) met ValueError
• Faila beigās: if __name__ == "__main__": bloks ar demonstrācijas izsaukumiem
Docstring piemērs:
def clamp(num, low, high):
Ierobežo skaitli norādītajā diapazonā.
Args:
num: skaitlis, ko ierobežot
low: minimālā robeža
high: maksimālā robeža
Returns:
int vai float: ierobežotā vērtība
Example:
10
0
>>> clamp(15, 0, 10)
>>> clamp(-5, 0, 10)
return max(low, min(num, high))"""

def greet(name):
    """Sveicina personu ar viņas vārdu.

    Args:
        name (str): Personas vārds.

    Returns:
        str: Sveiciens ar personas vārdu.

    Example:
        >>> greet("Anna")
        'Hello, Anna!'
    """
    if not isinstance(name, str):
        raise ValueError("Ievadei jābūt tekstam.")
    return f"Hello, {name}!"

def capitalize(text):
    """Pārvērš pirmo burtu lielo.

    Args:
        text (str): Ievades teksts.

    Returns:
        str: Teksts ar pirmo burtu lielo un pārējiem mazajiem.

    Example:
        >>> capitalize("hello")
        'Hello'
    """
    if not isinstance(text, str):
        raise ValueError("Ievadei jābūt tekstam.")
    if len(text) == 0:
        return ""
    return text[0].upper() + text[1:].lower()  

def validate_grade(grade):
    """Pārbauda, vai atzīme ir robežās no 0 līdz 100.
    Args:
        grade (int): Atzīme, ko pārbaudīt.
        Returns:
        bool: True, ja atzīme ir derīga, False pretējā gadījumā.
    Example:
        >>> validate_grade(85)
        True
        >>> validate_grade(-5)
        False
        >>> validate_grade(105)
        False
        """
    return 0 <= grade <= 100

def truncate(text, max_len=20):
    """Apgriež tekstu līdz norādītajam garumam un pievieno "..." ja nepieciešams.

    Args:
        text (str): Ievades teksts.
        max_len (int, optional): Maksimālais garums. Noklusējums ir 20.

    Returns:
        str: Apgriezts teksts ar "..." ja tas pārsniedz max_len.

    Example:
        >>> truncate("This is a long text that needs to be truncated.", 20)
        'This is a long te...'
    """
    if not isinstance(text, str):
        raise ValueError("Ievadei jābūt tekstam.")
    if not isinstance(max_len, int) or max_len < 0:
        raise ValueError("max_len jābūt nenegatīvam veselam skaitlim.")
    if len(text) <= max_len:
        return text
    return text[:max_len] + "..."

def count_words(text):
    """Saskaita vārdus tekstā.

    Args:
        text (str): Ievades teksts.

    Returns:
        int: Vārdu skaits tekstā.

    Example:
        >>> count_words("Hello world!")
        2
    """
    if not isinstance(text, str):
        raise ValueError("Ievadei jābūt tekstam.")
    words = text.split()
    return len(words)

def is_prime(num):
    """Pārbauda, vai skaitlis ir pirmskaitlis.

    Args:
        num (int): Skaitlis, ko pārbaudīt.
    Returns:
        bool: True, ja skaitlis ir pirmskaitlis, False pretējā gadījumā.
    Example:
        >>> is_prime(7)
        True
        >>> is_prime(10)
        False
    """
    if not isinstance(num, int) or num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def factorial(n):
    """Aprēķina faktoriālu skaitlim n.

    Args:
        n (int): Skaitlis, kuram aprēķināt faktoriālu. Jābūt n >= 0.

    Returns:
        int: Faktoriāla vērtība.

    Raises:
        ValueError: Ja n ir negatīvs.

    Example:
        >>> factorial(5)
        120
        >>> factorial(0)
        1
    """
    if not isinstance(n, int) or n < 0:
        raise ValueError("n jābūt nenegatīvam veselam skaitlim.")
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

def total(numbers):
    """Aprēķina saraksta skaitļu summu.

    Args:
        numbers (list of int or float): Skaitļu saraksts.

    Returns:
        int or float: Skaitļu summa.

    Example:
        >>> total([1, 2, 3, 4])
        10
    """
    if not all(isinstance(num, (int, float)) for num in numbers):
        raise ValueError("Visiem elementiem jābūt skaitļiem.")
    summa = 0
    for num in numbers:
        summa += num
    return summa

def average(numbers):
    """Aprēķina saraksta skaitļu vidējo aritmētisko.

    Args:
        numbers (list of int or float): Skaitļu saraksts.

    Returns:
        float: Skaitļu vidējais aritmētiskais.

    Raises:
        ValueError: Ja saraksts ir tukšs.

    Example:
        >>> average([1, 2, 3, 4])
        2.5
    """
    if not numbers:
        raise ValueError("Saraksts nedrīkst būt tukšs.")
    if not all(isinstance(num, (int, float)) for num in numbers):
        raise ValueError("Visiem elementiem jābūt skaitļiem.")
    summa = total(numbers)
    return summa / len(numbers)



if __name__ == "__main__":
    # Demonstrācijas izsaukumi
    print(greet("Anna"))
    print(capitalize("hello world"))
    print(validate_grade(85))
    print(truncate("This is a long text that needs to be truncated.", 20))
    print(count_words("Hello world! This is a test."))
    print(is_prime(7))
    print(factorial(5))
    print(total([1, 2, 3, 4]))
    print(average([1, 2, 3, 4]))