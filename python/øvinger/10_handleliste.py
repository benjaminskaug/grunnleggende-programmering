# ============================================================
# PROSJEKT 10 – HANDLELISTE
# ============================================================

handleliste = [
    "Melk",
    "Brød",
    "Egg",
    "Ost"
]

print("===== HANDLELISTE =====")

print(handleliste)


# ============================================================
# HENTE UT VARER
# ============================================================

print()
print(f"Første vare: {handleliste[0]}")
print(f"Andre vare: {handleliste[1]}")
print(f"Tredje vare: {handleliste[2]}")
print(f"Siste vare: {handleliste[-1]}")


# ============================================================
# LEGGE TIL VARER
# ============================================================

handleliste.append("Epler")
handleliste.append("Syltetøy")


print()
print("Etter at nye varer er lagt til:")
print(handleliste)


# ============================================================
# FJERNE EN VARE
# ============================================================

handleliste.remove("Egg")

print()
print("Etter at egg er fjernet:")
print(handleliste)


# ============================================================
# ENDRE EN VARE
# ============================================================

handleliste[0] = "Havremelk"

print()
print("Etter at melk er byttet:")
print(handleliste)


# ============================================================
# ANTALL VARER
# ============================================================

antall_varer = len(handleliste)

print()
print(f"Du har {antall_varer} varer på handlelisten.")


# ============================================================
# SJEKKE OM EN VARE FINNES
# ============================================================

if "Ost" in handleliste:
    print("Du skal kjøpe ost.")

else:
    print("Ost står ikke på handlelisten.")


# ============================================================
# SORTERE LISTEN
# ============================================================

handleliste.sort()

print()
print("Sortert handleliste:")
print(handleliste)