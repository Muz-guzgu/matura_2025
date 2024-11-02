
def wczytaj_dane_z_pliku(nazwa_pliku: str) -> list[str]:
    with open(nazwa_pliku) as obiekt_pliku:
        dane = obiekt_pliku.readlines()
    return [linia.split()[0] for linia in dane]

def main()->None:
    plik = r".\\dane\\slowa.txt"
    plik_przyklad = r".\\dane\\slowa_przyklad.txt"
    dane_z_pliku = wczytaj_dane_z_pliku(plik_przyklad)
    print(dane_z_pliku)

if __name__ == "__main__":
    main()