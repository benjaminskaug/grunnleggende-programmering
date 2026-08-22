# ============================================================
# PROSJEKT 13 – TERNINGKAST
# ============================================================

import random

antall_kast = int(input("Hvor mange ganger vil du kaste terningen? "))

kast = []

for _ in range(antall_kast):
    resultat = random.randint(1, 6)
    kast.append(resultat)

print()
print("===== TERNINGKAST =====")

for resultat in kast:
    print(f"Du fikk terningkast {resultat}.")


# ============================================================
# STATISTIKK
# ============================================================

print()

antall_seksere = kast.count(6)
print(f"Antall seksere: {antall_seksere}")

høyeste = max(kast)
laveste = min(kast)

print()
print(f"Høyeste kast: {høyeste}")
print(f"Laveste kast: {laveste}")

gjennomsnitt = sum(kast) / len(kast)

print()
print(f"Gjennomsnitt: {gjennomsnitt:.2f}")