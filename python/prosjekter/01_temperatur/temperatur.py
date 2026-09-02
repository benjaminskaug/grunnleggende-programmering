from collections.abc import Callable



def celsius_til_fahrenheit(temperatur: float) -> float:
    return temperatur * 9 / 5 + 32


def fahrenheit_til_celsius(temperatur: float) -> float:
    return (temperatur - 32) * 5 / 9


def hent_temperatur(melding: str) -> float:
    while True:
        try:
            return float(input(melding))
        except ValueError:
            print("Skriv inn et gyldig tall.")


def hent_valg() -> int:
    while True:
        try:
            return int(input("Velg konvertering: "))
        except ValueError:
            print("Skriv inn et gyldig tall.")


def vis_meny() -> None:
    print("\nTemperatur")
    print("1. Celsius til Fahrenheit")
    print("2. Fahrenheit til Celsius")
    print("3. Avslutt")


def konverter(
    melding: str,
    fra_enhet: str,
    til_enhet: str,
    konvertering: Callable[[float], float]
) -> None:
    temperatur = hent_temperatur(melding)
    resultat = konvertering(temperatur)
    
    print(f"{temperatur} {fra_enhet} = {resultat:.1f} {til_enhet}")



def main() -> None:
    while True:
        vis_meny()
        valg = hent_valg()

        match valg:
            case 1:
                konverter(
                    "Celsius: ",
                    "°C",
                    "°F",
                    celsius_til_fahrenheit
                )
            case 2:
                konverter(
                    "Fahrenheit: ",
                    "°F",
                    "°C",
                    fahrenheit_til_celsius
                )
            case 3:
                print("Ha det.")
                break
            case _:
                print("Ugyldig valg.")


if __name__ == "__main__":
    main()
