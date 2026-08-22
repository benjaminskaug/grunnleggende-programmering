# ============================================================
# PROSJEKT 09 – FLYPLASS
# ============================================================

destinasjon = input("Hvor skal du fly? ").lower()
bagasje = float(input("Hvor mange kilo bagasje har du? "))
har_pass = input("Har du boardingkort? (ja/nei) ").lower()

print()
print("===== INNSJEKKING =====")

# Sjekk boardingkort

if har_pass != "ja":
    print("Du må ha boardingkort for å gå videre.")

else:
    print("Boardingkort godkjent.")

    # Sjekk bagasje

    if bagasje <= 23:
        print("Bagasjen er innenfor grensen.")
        bagasjepris = 0

    elif bagasje <= 32:
        print("Du har ekstra bagasje.")
        bagasjepris = 300

    else:
        print("Bagasjen er for tung.")
        bagasjepris = 600

    # Finn destinasjon

    if destinasjon == "oslo":
        flytid = 1.0

    elif destinasjon == "bergen":
        flytid = 1.0

    elif destinasjon == "tromsø":
        flytid = 1.5

    elif destinasjon == "trondheim":
        flytid = 1.0

    else:
        flytid = 0

    # Vis informasjon om flyreisen

    if flytid > 0:
        print()
        print("===== FLYINFORMASJON =====")
        print(f"Destinasjon: {destinasjon.capitalize()}")
        print(f"Bagasje: {bagasje:.1f} kg")
        print(f"Ekstra bagasje: {bagasjepris} kr")
        print(f"Flytid: ca. {flytid:.1f} timer")

    else:
        print("Vi finner ikke informasjon om denne destinasjonen.")