"""
C daļā gan es izvēlējos nepārrakstīt ar roku, jo B daļā ja mainas studentu vārdi
un atzīmes, tā dēļ izvēlējos automatizēt un paņemt datus no B daļas.
"""
print("\n" + "\"A daļa — Saraksti:".center(80,"*") + "\n")
numbers = [1, 4, 23, 5, 21, 10, 3]
numbers.append(7) #pievieno elementu
numbers.pop(0) #dzēš elementu pēc indeksa, šajā gadījumā dzēš pirmo elementu (1)

summa = 0
total_numbers = 0
para_skaitli = []

for num in numbers: 
    summa += num 
    total_numbers += 1
    if num % 2 == 0: 
        print (f"{num} - pāra skaitlis")
        para_skaitli.append(num) #ieliekam pāra skaitli para_skaitli sarakstā
    else:
        print (f"{num} - nepāra skaitlis")


print(f"\nKopējais skaits: {total_numbers}")
print(f"Summa: {summa}")
print(f"Vidējais skaitlis: {summa / total_numbers}")
print(f"Pāra skaitļi: {para_skaitli}")

print("\n" + "B daļa — Vārdnīcas:".center(80,"*") + "\n")


students = {"Anna": 85, "Jānis": 72, "Līga": 95}
print(f"\nStudenti sākumā: {students}")
students["Pēteris"] = 78 #pievieno jaunu studentu
students["Jānis"] = 75 #maina esošu atzīmi

#grade = 0. <-- šis ir lieki, jo for ciklā tiek izveidots mainīgais grade, kurā glabāt.
max_grade = 0
best_student = ""
for name, grade in students.items():
    print(f"{name}: {grade}")
    if grade > max_grade:
        max_grade = grade
        best_student = name

print(f"\nLabākais students: {best_student} ({max_grade})")

print("\n" + "C daļa — Kombinācija:".center(80,"*") + "\n")

student_list = []
for name, grade in students.items():
    student_list.append({"name": name, "grade": grade})
high_achievers = []
for student in student_list:
    if student["grade"] >= 80:
        high_achievers.append(student)
for index, student in enumerate(high_achievers, start=1):
    print(f"{index}. {student['name']} — {student['grade']}")