# ============================================================
# PROSJEKT 12 – KAFÉ
# ============================================================

totalpris = 0

print("===== KAFÉ =====")
print("Meny:")
print("1 - Kaffe: 35 kr")
print("2 - Te: 30 kr")
print("3 - Kakestykke: 55 kr")
print("4 - Avslutt")

valg = input("Hva vil du bestille? ")

while valg != "4":

    if valg == "1":
        print("Du har bestilt kaffe.")
        totalpris += 35

    elif valg == "2":
        print("Du har bestilt te.")
        totalpris += 30

    elif valg == "3":
        print("Du har bestilt et kakestykke.")
        totalpris += 55

    else:
        print("Ugyldig valg.")

    print()
    print("1 - Kaffe: 35 kr")
    print("2 - Te: 30 kr")
    print("3 - Kakestykke: 55 kr")
    print("4 - Avslutt")

    valg = input("Hva vil du bestille? ")


print()
print("===== KVITTERING =====")
print(f"Totalpris: {totalpris} kr")
print("Takk for besøket!")
