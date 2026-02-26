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