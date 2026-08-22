# ============================================================
# PROSJEKT 14 – LOTTERI
# ============================================================

import random

print()
print("===== LOTTERI =====")

sjekk_tall = int(input("Hvilket tall tror du at du kommer til å få? "))

antall_tall = int(input("Hvor mange tall vil du trekke? "))

trekninger = []

for _ in range(antall_tall):
    tall = random.randint(1, 50)
    trekninger.append(tall)


print()
print("Trukne tall:")

for tall in trekninger:
    print(tall)

if sjekk_tall in trekninger:
    print()
    print(f"{sjekk_tall} ble trukket!")

else:
    print()
    print(f"{sjekk_tall} ble ikke trukket.")


# ============================================================
# SANNSYNLIGHET
# ============================================================

sannsynlighet = 1 - (49 / 50) ** antall_tall
prosent = sannsynlighet * 100

print()
print("===== SANNSYNLIGHET =====")

print(f"Sannsynligheten for å trekke {sjekk_tall} minst én gang:")
print(f"{prosent:.2f} %")


# ============================================================
# STATISTIKK
# ============================================================

print()
print("===== STATISTIKK =====")

print(f"Minste tall: {min(trekninger)}")
print(f"Største tall: {max(trekninger)}")


partall = 0
oddetall = 0

for tall in trekninger:

    if tall % 2 == 0:
        partall += 1
    
    else:
        oddetall += 1

print(f"Partall: {partall}")
print(f"Oddetall: {oddetall}")