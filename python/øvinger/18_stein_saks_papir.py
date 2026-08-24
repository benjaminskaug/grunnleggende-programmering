# ============================================================
# PROSJEKT 18 – STEIN, SAKS, PAPIR
# ============================================================

import random

valg = ["stein", "saks", "papir"]

spiller_poeng = 0
datamaskin_poeng = 0


print("===== STEIN, SAKS, PAPIR =====")
print("Skriv 'avslutt' for å avslutte.")
print()

while True:

    spiller = input("Velg stein, saks eller papir: ").lower()

    if spiller == "avslutt":
        break

    if spiller not in valg:
        print("Ugyldig ")
        continue

    datamaskin = random.choice(valg)
    print()
    print(f"Datamaskinen valgte: {datamaskin}")

    if spiller == datamaskin:
        print("Uavgjort")

    elif (
        spiller == "stein" and datamaskin == "saks"
        or spiller == "saks" and datamaskin == "papir"
        or spiller == "papir" and datamaskin == "stein"
    ):
        print("Du vant!")
        spiller_poeng += 1

    else:
        print("Datamaskinen vant!")
        datamaskin_poeng += 1  

    print()
    print(f"Spiller: {spiller_poeng}")
    print(f"Datamaskin: {datamaskin_poeng}")
    print()