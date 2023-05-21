class Trojkat:
    def __init__(self, a, b, c, h_a):
        self.bok_a = a
        self.b = b
        self.c = c
        self.h_a = h_a
        # self.obwod = a + b + c

    def obwod(self):
        return self.bok_a + self.b + self.c

    def pole(self):
        # TODO
        return 0



trojkat_rownoboczny = Trojkat(10, 10, 10, 8)
trojkat_oli = Trojkat(8, 6, 10, 4)

print(trojkat_rownoboczny.obwod())


print("--------------------------------")

class Student:
    def __init__(self, imie, nazwisko, numer_indeksu):
        self.imie = imie
        self.nazwisko = nazwisko
        self.numer_indeksu = numer_indeksu
        self.oceny = []

    def __str__(self):
        return f"{self.imie} {self.nazwisko} {self.numer_indeksu}"

    def __int__(self):
        return 1

    def dodaj_ocene(self, ocena):
        self.oceny.append(ocena)

    def zwroc_srednia(self):
        return sum(self.oceny) / len(self.oceny)


student_ola = Student("Aleksandra", "Wojewoda", 123123)
student_ola.dodaj_ocene(4.5)
student_ola.dodaj_ocene(5)

print(student_ola.oceny)