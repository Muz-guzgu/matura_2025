import math
from pydoc import resolve
def wczytaj_dane_z_pliku(nazwa_pliku: str)-> list[int]:
    'Funkcja czyta dane z pliku i wkłada je do listy zamieniając na int-y'
    with open(nazwa_pliku) as obiekt_plikowy:
        dane_z_pliku = obiekt_plikowy.readlines()
    return [int(line.split()[0]) for line in dane_z_pliku]


def zapisz_zadanie(nazwa_pliku: str, wyniki_zadania_4_1: str)-> None:
    with open(nazwa_pliku, 'w') as obiekt_plikowy:
        obiekt_plikowy.write(wyniki_zadania_4_1)


def czy_liczba_jest_pierwsza(liczba: int) -> bool:
    if liczba < 2:
        return False
    if liczba == 2:
        return True
    if liczba % 2 == 0:
        return False

    # sito Erastotenesa
    max_dzielnik = int(math.sqrt(liczba)) + 1
    for i in range(3, max_dzielnik, 2):
        if liczba % i == 0:
            return False
    return True


def zadanie_4_1(dane_z_pliku: list[int])-> list[int]:
    return [liczba for
            liczba in
            dane_z_pliku if
            100 <= liczba <= 5000 and czy_liczba_jest_pierwsza(liczba)]

def zamien_liste_na_napis(lista: list[int])-> str:
    return '\n'.join([str(element) for element in lista])


def odwroc_liczbe(liczba: int)-> int:
    return int(str(liczba)[::-1])


def zadanie_4_2(dane_z_pliku: list[int])-> list[int]:
    return [liczba
            for liczba
            in dane_z_pliku
            if czy_liczba_jest_pierwsza(liczba) and czy_liczba_jest_pierwsza(odwroc_liczbe(liczba))]

def zamien_liczbe_na_liste_cyfr(liczba: int)-> list[int]:
    return [int(cyfra) for cyfra in str(liczba)]

def licz_wage(liczba: str)-> int:
    liczba = str(liczba)
    ile_cyfr = len(liczba)
    while ile_cyfr > 1:
        liczba = str(sum([int(i) for i in liczba]))
        ile_cyfr = len(liczba)
    return int(liczba)


def zadanie_4_3(dane_z_pliku: list[str])-> int:
    wagi =[licz_wage(str(liczba))
            for liczba
            in dane_z_pliku]
    return wagi.count(1)

# Główna pętla programu
if __name__ == '__main__':
    # Wczytujemy dane (tylko jeden raz)
    plik = r".\\dane\\pierwsze.txt"
    plik_przyklad = r".\\dane\\pierwsze.txt"
    dane_z_pliku = wczytaj_dane_z_pliku(plik_przyklad)

    # rozwiązujemy zadania za pomocą funkcji i przypisujemy je do zmiennych
    wyniki_zadania_4_1 = zadanie_4_1(dane_z_pliku)
    wyniki_zadania_4_1_tekst_do_pliku = zamien_liste_na_napis(wyniki_zadania_4_1)

    wyniki_zadania_4_2 = zadanie_4_2(dane_z_pliku)
    wyniki_zadania_4_2_tekst_do_pliku = zamien_liste_na_napis(wyniki_zadania_4_2)

    wyniki_zadania_4_3 = zadanie_4_3(dane_z_pliku)

    # Wyniki zapisujemy do odpowiednich plików za pomocą jednej funkcji
    zapisz_zadanie(' wyniki4_1.txt', wyniki_zadania_4_1_tekst_do_pliku)
    zapisz_zadanie(' wyniki4_2.txt', wyniki_zadania_4_2_tekst_do_pliku)
    zapisz_zadanie(' wyniki4_3.txt', str(wyniki_zadania_4_3))
