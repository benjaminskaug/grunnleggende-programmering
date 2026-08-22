# ============================================================
# PROSJEKT 11 – MATVARER
# ============================================================

matvarer = [
    "Melk",
    "Brød",
    "Ost",
    "Epler",
    "Bananer"
]


print("===== MATVARER =====")

for matvare in matvarer:
    print(f"- {matvare}")


# ============================================================
# PRISER
# ============================================================

priser = [24.90, 39.90, 89.90, 34.90, 29.90]

print()
print("===== PRISER =====")

for pris in priser:
    print(f"{pris:.2f} kr")


# ============================================================
# MATVARE OG PRIS SAMMEN
# ============================================================

print()
print("===== PRODUKTER =====")

for matvare, pris in zip(matvarer, priser):
    print(f"{matvare}: {pris:.2f} kr")


# ============================================================
# BEREGNE TOTALPRIS
# ============================================================

total = 0

for pris in priser:
    total += pris

print()
print(f"Totalpris: {total:.2f} kr.")


# ============================================================
# ANTALL MATVARER
# ============================================================

antall = 0

for matvare in matvarer:
    antall += 1

print(f"Antall matvarer: {antall}")