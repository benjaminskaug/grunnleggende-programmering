# ============================================================
# PROSJEKT 19 – KONTAKTER
# ============================================================

kontakter = []

while True:

    print()
    print("===== KONTAKTER =====")
    print("1. Legg til kontakt")
    print("2. Vis kontakter")
    print("3. Søk etter kontakt")
    print("4. Avslutt")

    valg = input("Velg hva du vil gjøre: ")

    # ========================================================
    # LEGG TIL KONTAKT
    # ========================================================

    if valg == "1":

        navn = input("Navn: ")
        telefon = input("Telefonnummer: ")
        epost = input("E-postadresse: ")

        kontakt = {
            "navn": navn,
            "telefon": telefon,
            "epost": epost
        }

        kontakter.append(kontakt)

        print(f"{navn} ble lagt til.")


    # ========================================================
    # VIS KONTAKTER
    # ========================================================

    elif valg == "2":

        if len(kontakter) == 0:
            print("Ingen kontakter å vise.")

        else:
            print()
            print("===== KONTAKTER =====")

            for kontakt in kontakter:
                print(f"Navn: {kontakt['navn']}")
                print(f"Telefonnummer: {kontakt['telefon']}")
                print(f"E-postadresse: {kontakt['epost']}")
                print()


    # ========================================================
    # SØK ETTER KONTAKTER
    # ========================================================

    elif valg == "3":

        søk = input("Hvem vil du søke etter? ")

        funnet = False

        for kontakt in kontakter:

            if kontakt["navn"].lower() == søk.lower():
                print()
                print(f"Navn: {kontakt['navn']}")
                print(f"Telefonnummer: {kontakt['telefon']}")
                print(f"E-postadresse: {kontakt['epost']}")

                funnet = True
                break

        if not funnet:
            print()
            print("Fant ingen kontakt.")


    # ========================================================
    # AVSLUTT
    # ========================================================

    elif valg == "4":
        print("Avslutter programmet.")
        break

    else:
        print("Ugyldig valg.")
