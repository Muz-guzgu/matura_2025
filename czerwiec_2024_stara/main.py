import re


def wczytaj_dane_z_pliku(nazwa_pliku: str) -> list[str]:
    with open(nazwa_pliku) as obiekt_pliku:
        dane = obiekt_pliku.readlines()
    return [linia.split()[0] for linia in dane]

def zapisz_zadanie(nazwa_pliku: str, dane_do_zapisu: str) -> None:
    with open(nazwa_pliku, 'w') as obiekt_plikowy:
        obiekt_plikowy.write(dane_do_zapisu)

def zadanie_3_1(dane_z_pliku: list[str]) -> int:
    return sum([1 for line in dane_z_pliku if re.findall(r'k.t', line)])

def zadanie_3_2(dane_z_pliku: list[str])-> int:
    return sum([1 for line in dane_z_pliku if line == rot13(line)[::-1]])

def rot13(line: str)-> str:
    rot = []
    for litera in line:
        ord_litery = ord(litera)
        if ord_litery < 110:
            rot.append(chr(ord_litery + 13))
        else:
            rot.append(chr(ord_litery - 13))
    return  ''.join(rot)


def zadanie_3_3(dane_z_pliku: list[str])-> int:
    pass

def main()->None:
    plik = r".\\dane\\slowa.txt"
    plik_przyklad = r".\\dane\\slowa_przyklad.txt"
    dane_z_pliku = wczytaj_dane_z_pliku(plik_przyklad)

    wyniki_zadania_3_1 = zadanie_3_1(dane_z_pliku)
    wyniki_zadania_3_2 = zadanie_3_2(dane_z_pliku)
    wyniki_zadania_3_3 = zadanie_3_3(dane_z_pliku)
    print(wyniki_zadania_3_3)

    zapisz_zadanie('wyniki4.txt','')


if __name__ == "__main__":
    main()