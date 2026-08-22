# ============================================================
# PROSJEKT 06 – FOTBALLKAMP
# ============================================================

mål_hjemmelag = int(input("Hvor mange mål fikk hjemmelaget? "))
mål_bortelag = int(input("Hvor mange mål fikk bortelaget? "))

if mål_hjemmelag > mål_bortelag:
    print("Hjemmelaget vant!")

elif mål_hjemmelag < mål_bortelag:
    print("Bortelaget vant!")

else:
    print("Kampen endte uavgjort.")