# ============================================================
# PROSJEKT 22 – BLOMSTERBUTIKK
# ============================================================

blomster = {
    "rose": 35,
    "tulipan": 20,
    "lilje": 45,
    "solsikke": 30
}


def vis_meny():
    print()
    print("===== BLOMSTERBUTIKK =====")

    for blomst, pris in blomster.items():
        print(f"{blomst.capitalize()}: {pris} kr")


def beregn_pris(blomst, antall):
    return blomster[blomst] * antall


def vis_bukett(bestilling):
    print()
    print("===== BESTILLING =====")

    totalpris = 0

    for blomst, antall in bestilling.items():

        pris = beregn_pris(blomst, antall)
        totalpris += pris

        print(
            f"{blomst.capitalize()}: "
            f"{antall} stk. - {pris} kr"
        )

    print(f"Totalpris: {totalpris} kr")


bestilling = {}

vis_meny()

while True:

    blomst = input("Hvilken blomst vil du ha? (skriv 'ferdig' for å avslutte): ").lower()

    if blomst == "ferdig":
        break

    if blomst not in blomster:
        print("Denne blomsten finnes ikke på menyen.")
        continue

    antall = int(input("Hvor mange vil du ha? "))

    if antall <= 0:
        print("Antallet må være større enn 0.")
        continue

    if blomst in bestilling:
        bestilling[blomst] += antall

    else:
        bestilling[blomst] = antall


if len(bestilling) > 0:
    vis_bukett(bestilling)

else:
    print("Du bestilte ingen blomster.")
