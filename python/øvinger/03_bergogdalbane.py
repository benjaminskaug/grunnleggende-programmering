# ============================================================
# PROSJEKT 03 – BERG-OG-DAL-BANE
# ============================================================

høyde = int(input("Hvor høy er du i cm? "))

if høyde < 120:
    print("Du er for lav til å kjøre berg-og-dal-banen.")

elif høyde < 140:
    print("Du kan kjøre barnebanen.")

else:
    print("Du kan kjøre berg-og-dal-banen.")
