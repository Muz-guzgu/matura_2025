import re
from collections import Counter

# WCZYTANIE/ODCZYT DANYCH Z/DO PLIKU
def wczytaj_dane_z_pliku(nazwa_pliku: str) -> list[str]:
    with open(nazwa_pliku) as obiekt_pliku:
        dane = obiekt_pliku.readlines()
    return [linia.split()[0] for linia in dane]

def zapisz_zadanie(nazwa_pliku: str, dane_do_zapisu: str) -> None:
    with open(nazwa_pliku, 'w') as obiekt_plikowy:
        obiekt_plikowy.write(dane_do_zapisu)

# FUNKCJE ROZWIAZUJACE
def zadanie_3_1(dane_z_pliku: list[str]) -> int:
    return sum([1 for line in dane_z_pliku if re.findall(r'k.t', line)])

def zadanie_3_2(dane_z_pliku: list[str])-> int:
    return sum([1 for line in dane_z_pliku if line == rot13(line)[::-1]])

def zadanie_3_3(dane_z_pliku: list[str])-> list[str]:
    return [linia for linia in dane_z_pliku if czy_conajmniej_polowa(linia)]

# FUNKCJE POMOCNICZE
def rot13(line: str)-> str:
    rot = []
    for litera in line:
        ord_litery = ord(litera)
        if ord_litery < 110:
            rot.append(chr(ord_litery + 13))
        else:
            rot.append(chr(ord_litery - 13))
    return  ''.join(rot)

def czy_conajmniej_polowa(linia: str)-> bool:
    policzone_litery = Counter(linia)
    ile_najczestszych_liter = policzone_litery.most_common()[0][1]
    polowa = len(linia)/2
    if ile_najczestszych_liter >= polowa:
        return True
    return False

# GŁÓWNA FUNKCJA STERUJĄCA
def main()->None:
    plik = r".\\dane\\slowa.txt"
    plik_przyklad = r".\\dane\\slowa_przyklad.txt"
    dane_z_pliku = wczytaj_dane_z_pliku(plik_przyklad)

    wyniki_zadania_3_1 = zadanie_3_1(dane_z_pliku)
    wyniki_zadania_3_2 = zadanie_3_2(dane_z_pliku)
    wyniki_zadania_3_3 = zadanie_3_3(dane_z_pliku)

    string_do_pliku = (f'zadanie 3.1 {wyniki_zadania_3_1}\n' +
                       f'zadanie 3.2 {wyniki_zadania_3_2}\n' +
                       f'zadanie 3.3 {",".join(wyniki_zadania_3_3)}')

    zapisz_zadanie('wyniki3.txt',string_do_pliku)

# WYWOŁANIE FUNKCJI main()
if __name__ == "__main__":
    main()