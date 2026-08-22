# ============================================================
# PROSJEKT 08 – KINESISK RESTAURANT
# ============================================================

rett = input("Hva vil du bestille? ").lower()
antall = int(input("Hvor mange porsjoner vil du ha? "))

if rett == "wok":
    pris = 169

elif rett == "våruller":
    pris = 89

elif rett == "and":
    pris = 199

elif rett == "nudler":
    pris = 149

if pris > 0:
    totalpris = pris * antall

    print()
    print("-----BESTILLING-----")
    print(f"Rett: {rett.capitalize()}")
    print(f"Antall: {antall}")
    print(f"Pris per porsjon: {pris:.2f} kr")
    print(f"Totalpris: {totalpris:.2f} kr")