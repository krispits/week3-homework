"""
Uzdevums 1: Datu kolekcijas praksē
Mērķis: iepazīt sarakstus (list) un vārdnīcas (dict) — datu struktūras, kas nepieciešamas
visiem turpmākajiem uzdevumiem.
Izveido data_collections.py, kas:
A daļa — Saraksti:
• Izveido sarakstu ar 5+ skaitļiem; pievieno elementu ar .append(), dzēš ar .pop()
• Aprēķina saraksta summu un vidējo vērtību ar for ciklu (nelietojot sum()/len() — lai
saprastu mehāniku)
• Filtrē sarakstu: izveido jaunu sarakstu tikai ar pāra skaitļiem (for + if)
• Demonstrē šķēlumu (slice): pirmie 3, pēdējie 2, katrs otrais elements
B daļa — Vārdnīcas:
• Izveido vārdnīcu ar 3+ studentiem: {"Anna": 85, "Jānis": 72, "Līga": 95}
• Pievieno jaunu studentu; maina esošu atzīmi
• Iterē ar for name, grade in studenti.items(): un izvada katru
• Atrod studentu ar augstāko atzīmi (for cikls pa vārdnīcu)
C daļa — Kombinācija:
• Izveido sarakstu ar vārdnīcām: [{"name": "Anna", "grade": 85}, ...]
• Filtrē: tikai studenti ar atzīmi >= 80
• Izmanto enumerate() un f-strings formatētai izvadei: "1. Anna — 85"
python data_collections.py
# --- Saraksti ---
# Summa: 45, Vidējais: 9.0
# Pāra skaitļi: [2, 4, 6, 8, 10]
# Pirmie 3: [1, 2, 3], Pēdējie 2: [9, 10]
# --- Vārdnīcas ---
# Anna: 85
# Jānis: 72
# ...
# Labākais students: Līga (95)
# --- Studenti ar atzīmi >= 80 ---
# 1. Anna — 85
# 2. Līga — 95
"""