# zadanie 1.1
hello = "Hello"
student = "Ola"
# oczekiwany rezultat: Hello Ola
# wykorzystaj w princie zmienne hello i student
print("Hello Kasia")
print("{} {}".format(hello, student))

# zadanie 1.2
hello = "Hello"
student = input("Podaj imię osoby, którą chcesz przywitać: ")
komunikat = "{} {}".format(hello, student)
print(komunikat)

# zadanie 1.4
studenci = ["Ania", "Kuba", "Piotr", "Jan"]
# policz liczbe studentow w tablicy studenci
liczba_studentow = len(studenci)
print("Liczba studentow wynosi:", liczba_studentow)

# zadanie 1.5
liczba = 3
potega = 4

wynik = liczba ** potega

print("Wynik wynosi:", wynik)

# zadanie 1.6
ciag_znakow = "edbw(hdakqas(skqskahb))adwndwb(wgwidn()dsqwhjdw)"
liczba_nawiasow_otwierajacych = ciag_znakow.count("(")

print("Liczba nawiasow otwierajacych wynosi:", liczba_nawiasow_otwierajacych)

# zadanie 1.7
studenci = ["Anna Szczesny", "Tomasz Nijaki", "Barbara Kowalska", "Jan Niezbedny"]

# Sortuj studentów alfabetycznie
studenci_posortowani = sorted(studenci)

print("Alfabetyczna lista studentów wynosi: ")
for student in studenci_posortowani:
    print(student)


# zadanie 1.8
studenci = ["Anna Szczesny", "Tomasz Nijaki", "Barbara Kowalska", "Jan Niezbedny"]

# Sortuj studentów alfabetycznie po nazwisku
studenci_posortowani = sorted(studenci, key=lambda x: x.split()[-1])

print("Alfabetyczna lista studentów wynosi: ")
for student in studenci_posortowani:
    print(student)

# zadanie 1.9
studenci = ["Anna Szczesny", "Tomasz Nijaki", "Barbara Kowalska", "Jan Niezbedny"]

liczba_n = 0
for student in studenci:
    if student.split()[-1][0].lower() == "n":
        liczba_n += 1

print("Liczba studentów na N wynosi:", liczba_n)


# zadanie 1.10
wykres_1 = [[2, 4], [4, 4], [6, 4]]
wykres_2 = [[2, 3], [4, 4], [6, 5]]
wykres_3 = [[2, 3], [4, 3], [5, 4]]


# Funkcja sprawdzająca, czy dla danych punktów można wyznaczyć funkcję liniową
def sprawdz_czy_funkcja_liniowa(punkty):
    x1, y1 = punkty[0]
    x2, y2 = punkty[1]
    x3, y3 = punkty[2]

    if (y2 - y1) / (x2 - x1) == (y3 - y2) / (x3 - x2):
        return True
    else:
        return False


wykres_1_funkcja_liniowa = sprawdz_czy_funkcja_liniowa(wykres_1)
wykres_2_funkcja_liniowa = sprawdz_czy_funkcja_liniowa(wykres_2)
wykres_3_funkcja_liniowa = sprawdz_czy_funkcja_liniowa(wykres_3)

if wykres_1_funkcja_liniowa:
    print("Dla punktów w wykres_1 można wyznaczyć funkcję liniową.")
else:
    print("Dla punktów w wykres_1 nie można wyznaczyć funkcji liniowej.")

if wykres_2_funkcja_liniowa:
    print("Dla punktów w wykres_2 można wyznaczyć funkcję liniową.")
else:
    print("Dla punktów w wykres_2 nie można wyznaczyć funkcji liniowej.")

if wykres_3_funkcja_liniowa:
    print("Dla punktów w wykres_3 można wyznaczyć funkcję liniową.")
else:
    print("Dla punktów w wykres_3 nie można wyznaczyć funkcji liniowej.")