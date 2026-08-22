# ============================================================
# PROSJEKT 15 – GJETT TALLET
# ============================================================

import random


hemmelig_tall = random.randint(1, 100)
forsøk = 0

print("===== GJETT TALLET =====")
print("Jeg tenker på et tall mellom 1 og 100.")

gjett = int(input("Hva er ditt første gjett? "))

while gjett != hemmelig_tall:

    forsøk += 1

    if gjett < hemmelig_tall:
        print("For lavt!")
    
    else:
        print("For høyt!")
    
    gjett = int(input("Prøv igjen: "))

forsøk += 1

print()
print("Riktig!")
print(f"Det hemmelige tallet var {hemmelig_tall}.")
print(f"Du brukte {forsøk} forsøk.")