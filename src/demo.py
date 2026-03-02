"""
Mērķis: parādīt, ka visi moduļi strādā kopā; praktizēt import no dažādiem failiem.
Izveido demo.py, kas:
• Importē funkcijas no utils.py un validators.py
• Izsauc vismaz 5 dažādas funkcijas ar dažādām ievadēm
• Demonstrē gan veiksmīgus, gan kļūdainus gadījumus (try/except)
• Formatēta izvade ar f-strings, kas parāda funkcijas nosaukumu, ievadi un rezultātu
python demo.py
# === Utils demonstrācija ===
# capitalize('hello') → 'Hello'
# clamp(15, 0, 10) → 10
# is_prime(17) → True
# average([10, 20, 30]) → 20.0
# factorial(-1) → ValueError: n nevar būt negatīvs
#
# === Validators demonstrācija ===
# is_email('test@test.lv') → True
# is_strong_password('abc') → False
# is_valid_date('2025-13-01') → False
"""    
from utils import greet, capitalize,  average
from validators import is_strong_password, is_valid_date

print("=== Utils demonstrācija ===")
try:    
    name = "rīga"
    greeting = greet(name)
    print(f"greet('{name}') → '{greeting}'")
    
    text = "hello"
    capitalized = capitalize(text)
    print(f"capitalize('{text}') → '{capitalized}'")
     
    numbers = [10, 20, 30]
    avg = average(numbers)
    print(f"average({numbers}) → {avg}")

except ValueError as e:
    print(f"factorial(-1) → ValueError: {e}")

print("\n=== Validators demonstrācija ===")

password = "abc"
is_valid = is_strong_password(password)
print(f"is_strong_password('{password}') → {is_valid}")

date = "2025-13-01"
is_valid = is_valid_date(date)
print(f"is_valid_date('{date}') → {is_valid}")
