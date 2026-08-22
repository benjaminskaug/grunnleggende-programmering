# ============================================================
# PROSJEKT 02 – KINO
# ============================================================

film = input("Hvilken film vil du se? ")
sal = input("Hvilken sal skal du bruke? ")

antall_billetter = int(input("Hvor mange billetter vil du kjøpe? "))
pris_per_billett = float(input("Hva koster én billett? "))

totalpris = antall_billetter * pris_per_billett

print()
print("----- KINOBILLETTER -----")
print(f"Film: {film}")
print(f"Sal: {sal}")
print(f"Antall billetter: {antall_billetter}")
print(f"Pris per billett: {pris_per_billett:.2f} kr")
print(f"Totalpris: {totalpris:.2f} kr")
