from random import randint
beine = 94
köpfe = 35
huener_beine = 2
kanienchen_beine = 4
for i in range(1000000000000):
    x = randint(1, 35)
    y = randint(1, 35)
    erg_h = x*huener_beine + y*kanienchen_beine
    if erg_h == 94 and x +y == 35:
        print(x, y)
        break