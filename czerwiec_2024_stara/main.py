import re


def wczytaj_dane_z_pliku(nazwa_pliku: str) -> list[str]:
    with open(nazwa_pliku) as obiekt_pliku:
        dane = obiekt_pliku.readlines()
    return [linia.split()[0] for linia in dane]


def zadanie_4_1(dane_z_pliku: list[str]) -> int:
    return sum([1 for line in dane_z_pliku if re.findall(r'k.t', line)])


def zapisz_zadanie(nazwa_pliku: str, dane_do_zapisu: str) -> None:
    with open(nazwa_pliku, 'w') as obiekt_plikowy:
        obiekt_plikowy.write(dane_do_zapisu)


def zadanie_4_2(dane_z_pliku: list[str])-> list[str]:
    result = []
    for line in dane_z_pliku:
        print(line)
        matches = re.finditer(r'e...e', line)
        result += [match.group(1) for match in matches if match.group(1)]
    return result


def rot13(line: str)-> str:
    rot = []

    for litera in line:
        print(litera, litera)

def zadanie_4_3(dane_z_pliku: list[str])-> int:
    return sum([1 for line in dane_z_pliku if rot13(line) == rot13(line)][::-1])


def main()->None:
    plik = r".\\dane\\slowa.txt"
    plik_przyklad = r".\\dane\\slowa_przyklad.txt"
    dane_z_pliku = wczytaj_dane_z_pliku(plik_przyklad)

    wyniki_zadania_4_1 = zadanie_4_1(dane_z_pliku)
    zapisz_zadanie('wyniki4.txt',str(wyniki_zadania_4_1))

    # wyniki_zadania_4_2 = zadanie_4_2(dane_z_pliku)
    # print(wyniki_zadania_4_2)

    wyniki_zadania_4_3 = zadanie_4_3(dane_z_pliku)
    print(wyniki_zadania_4_3)

if __name__ == "__main__":
    main()