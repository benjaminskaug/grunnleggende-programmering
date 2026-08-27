# ============================================================
# PROSJEKT 21 – BILVERKSTED
# ============================================================

arbeid_pris = 950

def vis_meny():
    print()
    print("===== BILVERKSTED =====")
    print("1. Oljeskift       2000 kr")
    print("2. Dekkskift       800 kr")
    print("3. Bremseservice   2500 kr")
    print("4. EU-kontroll     1200 kr")

def hvilken_service(valg):
    service = {
        "1": ("Oljeskift", 2000),
        "2": ("Dekkskift", 800),
        "3": ("Bremseservice", 2500),
        "4": ("EU-kontroll", 1200)
    }

    return service.get(valg)

def beregn_total(servicepris, timer):
    return servicepris + (timer * arbeid_pris)

def vis_kvittering(registreringsnummer, service, timer, total):
    print()
    print("===== KVITTERING =====")
    print(f"Registreringsnummer: {registreringsnummer}")
    print(f"Service: {service}")
    print(f"Arbeidstid: {timer} timer")
    print(f"Arbeidspris: {timer * arbeid_pris} kr")
    print(f"Totalpris: {total} kr")


registreringsnummer = input("Registreringsnummer: ")

vis_meny()


valg = input("Velg service: ")

resultat = hvilken_service(valg)

if resultat is None:
    print("Ugyldig valg.")

else:
    service, servicepris = resultat

    timer = float(input("Hvor mange timer tar arbeidet? "))

    total = beregn_total(servicepris, timer)

    vis_kvittering(
        registreringsnummer,
        service,
        timer,
        total
    )
