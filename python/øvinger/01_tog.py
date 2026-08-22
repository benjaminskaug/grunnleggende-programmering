# ============================================================
# PROSJEKT 01 – TOG
# ============================================================

tognummer = "R50"
destinasjon = "Nelaug stasjon"
plattform = 1
stoppesteder = [
    "Stoa",
    "Bråstad",
    "Rise",
    "Blakstad",
    "Froland",
    "Bøylestad",
    "Flaten"
]
reisetid = 37
sitteplasser = 235
avgangstid = "10:10"
forsinket = False
strøm = True
internett = True
toalett = True
billettpris = 55.50


print("----- TOGINFORMASJON -----")
print(f"Tognummer: {tognummer}")
print(f"Destinasjon: {destinasjon}")
print(f"Plattform: {plattform}")
print(f"Stoppesteder: {stoppesteder}")
print(f"Reisetid: {reisetid} minutter")
print(f"Sitteplasser: {sitteplasser}")
print(f"Avgangstid: {avgangstid}")
print(f"Billettpris: {billettpris:.2f} kr")
print(f"Forsinket: {forsinket}")
print(f"Strøm: {strøm}")
print(f"Internett: {internett}")
print(f"Toalett: {toalett}")
