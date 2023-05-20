# trapez
a = 10
b = 20
h = 12

obwod = a + b + 2 * math.sqrt(((b - a) / 2)**2 + h**2)
pole = ((a + b) * h) / 2

print("Obwod trapezu wynosi " + str(obwod) + ", a pole wynosi " + str(pole) + ".")
