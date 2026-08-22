# ============================================================
# PROSJEKT 05 – BIBLIOTEK
# ============================================================

alder = int(input("Hvor gammel er du? "))
har_lånekort = input("Har du lånekort? (ja/nei) ").lower()
boken_ledig = input("Er boken ledig? (ja/nei) ").lower()

if alder >= 18 and har_lånekort == "ja" and boken_ledig == "ja":
    print("Du kan låne boken.")

elif har_lånekort != "ja":
    print("Du må ha lånekort for å låne bøker.")

elif boken_ledig != "ja":
    print("Boken er allerede utlånt.")

else:
    print("Du kan ikke låne boken.")