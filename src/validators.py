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