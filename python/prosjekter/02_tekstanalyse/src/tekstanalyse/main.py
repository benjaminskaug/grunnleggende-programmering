def finn_antall_tegn(tekst: str) -> int:
    return len(tekst)


def finn_antall_ord(ordliste: list[str]) -> int:
    return len(ordliste)


def finn_unike_ord(ordliste: list[str]) -> int:
    return len(set(ordliste))


def finn_lengste_ord(ordliste: list[str]) -> str:
    if not ordliste:
        return "Ingen ord"

    return max(ordliste, key=len)


def lag_frekvens(ordliste: list[str]) -> dict[str, int]:
    frekvens = {}

    for ordet in ordliste:
        frekvens[ordet] = frekvens.get(ordet, 0) + 1

    return frekvens


def finn_mest_brukte_ord(frekvens: dict[str, int]) -> str:
    if not frekvens:
        return "Ingen ord"

    mest_brukt = max(frekvens.items(), key=lambda par: par[1])
    return mest_brukt[0]


def hent_tekst() -> str:
    while True:
        tekst = input("Skriv inn en tekst: ").strip()

        if not tekst:
            print("Skriv inn en tekst:")
            continue

        return tekst


def lag_ordliste(tekst: str) -> list[str]:
    ordliste = []

    for ordet in tekst.split():
        ordet = ordet.strip(".,!?").lower()

        if ordet:
            ordliste.append(ordet)

    return ordliste


def vis_utskrift(tekst: str, ordliste: list[str], frekvens: dict[str, int]) -> None:
    print()
    print("Tekstanalyse")
    print(f"Antall tegn: {finn_antall_tegn(tekst)}")
    print(f"Antall ord: {finn_antall_ord(ordliste)}")
    print(f"Antall unike ord: {finn_unike_ord(ordliste)}")
    print(f"Lengste ord: {finn_lengste_ord(ordliste).capitalize()}")
    print(f"Mest brukte ord: {finn_mest_brukte_ord(frekvens).capitalize()}")


def main() -> None:
    tekst = hent_tekst()
    ordliste = lag_ordliste(tekst)
    frekvens = lag_frekvens(ordliste)

    vis_utskrift(tekst, ordliste, frekvens)


if __name__ == "__main__":
    main()