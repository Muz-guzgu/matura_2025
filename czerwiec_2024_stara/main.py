import re


def wczytaj_dane_z_pliku(nazwa_pliku: str) -> list[str]:
    with open(nazwa_pliku) as obiekt_pliku:
        dane = obiekt_pliku.readlines()
    return [linia.split()[0] for linia in dane]


def zadanie_4_1(dane_z_pliku: list[str]) -> int:
    return sum([1 for line in dane_z_pliku if re.findall(r'k.t', line)])


def main()->None:
    plik = r".\\dane\\slowa.txt"
    plik_przyklad = r".\\dane\\slowa_przyklad.txt"
    dane_z_pliku = wczytaj_dane_z_pliku(plik_przyklad)

    wyniki_zadania_4_1 = zadanie_4_1(dane_z_pliku)
    print(wyniki_zadania_4_1)
if __name__ == "__main__":
    main()