####################
## KLASA SAMOCHOD ##
####################


class Samochod:
    def __init__(self, marka, model, rocznik, kolor, pojemnosc_silnika, przebieg, cena, stan):
        self.marka = marka
        self.model = model
        self.rocznik = rocznik 
        self.kolor = kolor
        self. pojemnosc_silnika = pojemnosc_silnika
        self.przebieg = przebieg
        self.cena = cena
        self.stan = stan


    def __str__(self):
        stan = "Bezwypadkowy" if self.stan else "Powypadkowy"
        return f"Samochod: {self.marka} {self.model}, Rocznik: {self.rocznik}, Kolor: {self.kolor}, Pojemnosc {self.pojemnosc_silnika}, Przebieg: {self.przebieg}, Cena: {self.cena}, Stan: {stan}"

    
    def sprawdz_przebieg(self):
        if self.przebieg < 100000:
            return "Niski przebieg"
        elif self.przebieg < 200000:
            return "Sredni przebieg"
        else:
            return "Wysoki przebieg"

    def oblicz_wartosc(self):
         return self.cena * 0.9 if (self.rocznik >= 2015) and (self.stan == "Bezwypadkowy") else self.cena * 0.7
        

samochod_1 = Samochod("Zygzak", "McQueen", 2006, "Czerrwony", 1.4, 210000, 40000, False)
samochod_2 = Samochod("Jackson ", "Storm ", 2017, "Srebrny", 1.6, 160000, 60000, True)

print(samochod_1)
print(samochod_1.sprawdz_przebieg())
print(samochod_1.oblicz_wartosc())

print(samochod_2)
print(samochod_2.sprawdz_przebieg())
print(samochod_2.oblicz_wartosc())




####################
## KLASA PILKARZ ##
####################

class Pilkarz: 
    def __init__(self, imie, nazwisko, klub, pozycja, numer, wiek, wzrost, waga, gole, asysty): 
        self.imie = imie
        self.nazwisko = nazwisko
        self.klub = klub
        self.pozycja = pozycja
        self.numer = numer
        self.wiek = wiek 
        self.wzrost = wzrost
        self.waga = waga 
        self.gole = gole 
        self.asysty = asysty 

    def __str__(self):
        return f"Pilkarz: {self.imie } {self.nazwisko } \n Klub: {self.klub}  \n Pozycja: {self.pozycja} \n Numer: {self.numer}  \n Wiek: {self.wiek} \n Liczba gole w lidze: {self.gole} \n Liczba asyst w lidze: {self.asysty}"
    
    def czy_mlody(self):
        return self.wiek < 27

    def oblicz_bmi(self):
        wzrost_metry = self.wzrost / 100
        bmi = self.waga / (wzrost_metry ** 2)
        return round(bmi, 2)

    def punktacja_kanadyjska(self):
        return self.gole + self.asysty


piłkarz_1 = Pilkarz("Robert", "Lewandowski", "FC Barcelona", "Napastnik", 9, 33, 185, 80, 23, 7)
piłkarz_2 = Pilkarz("Lionel", "Messi", "Paris Saint-Germain", "Napastnik", 30, 34, 170, 72, 16, 16)

print(piłkarz_1)
print(piłkarz_1.czy_mlody())
print(piłkarz_1.oblicz_bmi())
print(piłkarz_1.punktacja_kanadyjska())

print(piłkarz_2)
print(piłkarz_2.czy_mlody())
print(piłkarz_2.oblicz_bmi())
print(piłkarz_2.punktacja_kanadyjska())
