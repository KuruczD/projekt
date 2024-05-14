from datetime import datetime
from abc import ABC, abstractmethod

class Szoba(ABC):
    def __init__(self, ar, szobaszam):
        self.ar = ar
        self.szobaszam = szobaszam
        self.foglalasok = []

    @abstractmethod
    def get_szoba_tipus(self):
        pass

    def foglalas(self, datum):
        self.foglalasok.append(datum)

    def lemondas(self, datum):
        if datum in self.foglalasok:
            self.foglalasok.remove(datum)
            print("Foglalás sikeresen törölve.")
        else:
            print("Nem található foglalás ezen a dátumon.")

    def listaz_foglalasok(self):
        if self.foglalasok:
            print(f"Foglalások a(z) {self.szobaszam} szobában:")
            for foglalas in self.foglalasok:
                print(f"- {foglalas.strftime('%Y-%m-%d')}")
        else:
            print("Nincsenek foglalások ebben a szobában.")

class EgyagyasSzoba(Szoba):
    def __init__(self, ar, szobaszam):
        super().__init__(ar, szobaszam)

    def get_szoba_tipus(self):
        return "Egyágyas szoba"

class KetagyasSzoba(Szoba):
    def __init__(self, ar, szobaszam):
        super().__init__(ar, szobaszam)

    def get_szoba_tipus(self):
        return "Kétágyas szoba"

class Szalloda:
    def __init__(self, nev):
        self.nev = nev
        self.szobak = []

    def add_szoba(self, szoba):
        self.szobak.append(szoba)

    def foglalas(self, szobaszam, datum):
        for szoba in self.szobak:
            if szoba.szobaszam == szobaszam:
                if datum in szoba.foglalasok:
                    print("Ez a szoba már foglalt ezen a dátumon.")
                    return
                try:
                    datum_obj = datetime.strptime(datum, "%Y-%m-%d")
                    szoba.foglalas(datum_obj)
                    print("Foglalás sikeresen rögzítve.")
                    return
                except ValueError:
                    print("Hibás dátum formátum. Kérlek, használj éééé-hh-nn formátumot.")
                    return
        print("Nem található ilyen szoba.")

    def lemondas(self, szobaszam, datum):
        for szoba in self.szobak:
            if szoba.szobaszam == szobaszam:
                try:
                    datum_obj = datetime.strptime(datum, "%Y-%m-%d")
                    szoba.lemondas(datum_obj)
                    return
                except ValueError:
                    print("Hibás dátum formátum. Kérlek, használj éééé-hh-nn formátumot.")
                    return
        print("Nem található ilyen szoba.")

    def listaz_foglalasok(self):
        print(f"Foglalások a(z) {self.nev} szállodában:")
        for szoba in self.szobak:
            szoba.listaz_foglalasok()

def main():
    # Szálloda, szobák és foglalások létrehozása
    szalloda = Szalloda("Luxus Hotel")
    szoba1 = EgyagyasSzoba(10000, "101")
    szoba2 = KetagyasSzoba(15000, "102")
    szoba3 = EgyagyasSzoba(12000, "103")
    szalloda.add_szoba(szoba1)
    szalloda.add_szoba(szoba2)
    szalloda.add_szoba(szoba3)
    szalloda.foglalas("101", "2024-05-10")
    szalloda.foglalas("102", "2024-05-12")
    szalloda.foglalas("101", "2024-05-15")
    szalloda.foglalas("103", "2024-05-20")
    szalloda.foglalas("103", "2024-05-25")

    # Felhasználói interfész
    while True:
        print("\nVálassz műveletet:")
        print("1. Foglalás")
        print("2. Lemondás")
        print("3. Foglalások listázása")
        print("4. Kilépés")
        valasztas = input("Művelet kiválasztása (1/2/3/4): ")

        if valasztas == "1":
            print("\nEgyágyas\n\n"+szoba1.szobaszam,"Ár :",szoba1.ar,"Ft","\n"+szoba3.szobaszam,"Ár :",szoba3.ar,"Ft","\n"+"\nKétágyas\n\n"+szoba2.szobaszam,"Ár :",szoba2.ar,"Ft","\n")
            szobaszam = input("Add meg a foglalni kívánt szoba számát: ")
            datum = input("Add meg a foglalás dátumát (éééé-hh-nn): ")
            szalloda.foglalas(szobaszam, datum)
        elif valasztas == "2":
            szobaszam = input("Add meg a lemondani kívánt foglalás szoba számát: ")
            datum = input("Add meg a foglalás dátumát (éééé-hh-nn): ")
            szalloda.lemondas(szobaszam, datum)
        elif valasztas == "3":
            szalloda.listaz_foglalasok()
        elif valasztas == "4":
            print("Kilépés...")
            break
        else:
            print("Érvénytelen választás.")

if __name__ == "__main__":
    main()
