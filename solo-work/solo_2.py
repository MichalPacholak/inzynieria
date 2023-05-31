## kwadrat

def kwadrat(bok):
    pole = bok * bok 
    obwod = 4 * bok 
    return pole, obwod 
print(f'Pole i obwod wynosza: {kwadrat(5)}')

##trapez

def trapez(podst_a, podst_b, h, bok_c, bok_d):
    pole = (podst_a + podst_b) * h / 2
    obwod = podst_a + podst_b + bok_c + bok_d
    return pole, obwod
print(f'Pole i obwod wynosza: {trapez(5, 8, 4, 6, 7)}')