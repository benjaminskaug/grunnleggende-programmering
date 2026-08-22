# ============================================================
# PROSJEKT 07 – KLESBUTIKK
# ============================================================

plagg = input("Hvilket plagg vil du kjøpe? ").lower()
størrelse = input("Hvilken størrelse bruke du? ").upper()
på_lager = input("Er plagget på lager? (ja/nei)").lower()

if not på_lager == "ja":
    print("Beklager, plagget er utsolgt.")

elif størrelse == "M" or størrelse == "L":
        print(f"Du kan kjøpe {plagg} i størrelse {størrelse}.")

else:
    print(f"{plagg.capitalize()} finnes ikke i denne størrelsen.")