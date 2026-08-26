# ============================================================
# PROSJEKT 20 – ISKREM
# ============================================================

def vis_meny():
    print()
    print("===== ISKREM-MENY =====")
    print("1. Vanilje      30 kr")
    print("2. Sjokolade    35 kr")
    print("3. Jordbær      35 kr")
    print("4. Pistasj      40 kr")


def hvilken_pris(valg):
    if valg == "1":
        return 30

    elif valg == "2":
        return 35

    elif valg == "3":
        return 35

    elif valg == "4":
        return 40

    else:
        return 0


def vis_bestilling(smaksvalg, kuler, totalpris):
    print()
    print("===== BESTILLING =====")
    print(f"Smak: {smaksvalg}")
    print(f"Kuler: {kuler}")
    print(f"Totalpris: {totalpris} kr")


vis_meny()

valg = input("Hvilke smak vil du ha? ")
kuler = int(input("Hvor mange kuler vil du ha? "))

pris = hvilken_pris(valg)

if pris == 0:
    print("Ugyldig valg.")

else:
    totalpris = pris * kuler

    if valg == "1":
        smak = "Vanilje"

    elif valg == "2":
        smak = "Sjokolade"

    elif valg == "3":
        smak = "Jordbær"

    else:
        smak = "Pistasj"

    vis_bestilling(smak, kuler, totalpris)