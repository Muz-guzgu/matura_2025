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
            czy_liczba_jest_pierwsza(liczba) and 100 <= liczba <= 5000]

# Główna pętla programu
def zamien_liste_na_napis(lista: list[int])-> str:
    return '\n'.join([str(element) for element in lista])


if __name__ == '__main__':
    # Wczytujemy dane (tylko jeden raz)
    dane_z_pliku = wczytaj_dane_z_pliku(r".\\dane\\liczby_przyklad.txt")

    # rozwiązujemy zadania za pomocą funkcji i przypisujemy je do zmiennych
    wyniki_zadania_4_1 = zadanie_4_1(dane_z_pliku)
    wyniki_zadania_4_1_tekst_do_pliku = zamien_liste_na_napis(wyniki_zadania_4_1)



    # Wyniki zapisujemy do odpowiednich plików za pomocą jednej funkcji
    zapisz_zadanie(' wyniki4_1.txt', wyniki_zadania_4_1_tekst_do_pliku)
    # zapisz_zadanie(' wyniki4_2.txt')
    # zapisz_zadanie(' wyniki4_3.txt')
    # zapisz_zadanie(' wyniki4_4.txt')