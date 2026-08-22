# ============================================================
# PROSJEKT 04 – MATBUTIKK
# ============================================================

matvare = input("Hvilken matvare vil du kjøpe? ").lower()
antall = int(input("Hvor mange vil du kjøpe? "))

if matvare == "melk":
    pris = 24.90

elif matvare == "brød":
    pris = 39.90

elif matvare == "ost":
    pris = 89.90

else:
    pris = 0
    print("Vi har ikke denne matvaren")

if pris > 0:
    totalpris = pris * antall

    print()
    print("-----KVITTERING-----")
    print(f"Matvare: {matvare}")
    print(f"Antall: {antall}")
    print(f"Pris per stykk: {pris:.2f} kr")
    print(f"Totalpris: {totalpris:.2f} kr")