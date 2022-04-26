#eine for schleife, die alle zahlen von 0 bis 9 ausgibt     
# for i in range(10):
#     print(i)

# #eine for schleife die alle zahlen von 0 bis 50 ausgibt
# p = 0

# for i in range(50):
#     p +=1
#     print(p)

# #eine for schleife die alle Zahlen von 10 bis 25
# p = 10

# for i in range(16):
#     print(p)
#     p +=1

# #for schleife die alle zahlen von 50 bis 150
# for i in range(101):
#     i += 50
#     print(i)

#eine for schleife die alle zahlen von 100 bis 0 ausgibt
# for i in range(100):
#     print(100-i)

# #eine for schleife die alle zahlen von 50 bis -50
# for i in range(101):
#     print(50-i)

# #eine for schleife die alle zahlen von 0 - 20 in 2er schritten ausgibt
# for i in range(10):
#     print(i * 2)

#eine for schleife die alle zahlen von 250 bis 750 in 5er schritten ausgibt
# for i in range(100):
#     print(i * 5 + 250)

#eine for schleife die alle quadratzahlen bis 225 ausgibt
# for i in range(16):
#     print(i * i)

#eine for schleife die alle 2er potenzen ausgibt



# liste = [0]
# for i in range(25):
#     liste.append(i+1)

# print(liste)

# #eine for schleife die alle 2er potenzen bis 8192 erstellt
#liste = [1]
#for i in range(13):
    #liste.append(liste[i] * 2)

#print(liste)
#eine for schleife die folgende sternchenfigur  ausgibt
#**********
#*********
#********
#*******
#******
#*****
#****
#***
#**
#*
# for i in range(10):
#     print('*')and print('*')and print('*')and print('*')and print('*')and print('*')and print('*')and print('*')and print('*')and print('*')

#auf einem bauernhof werden 35 Köpfe une 94 Beine gezählt.
#wie viele Kanienchen und wie viele Hüner leben dort???
# from random import randint
# beine = 94
# köpfe = 35
# huener_beine = 2
# kanienchen_beine = 4
# for i in range(10000000):
#     x = randint(1, 20)
#     y = randint(1, 20)
#     erg_h = x*huener_beine + y*kanienchen_beine
#     if erg_h == 94 and x +y == 35:
#         print(huener_beine, kanienchen_beine)
#         break

# beine = 94
# köpfe = 35
# huener_beine = 2
# kanienchen_beine = 4
# for h in range(36):
#     for k in range(36):
#         pa = h*huener_beine /2
#         pa2 = k*kanienchen_beine /4
#         ergebnis = h*huener_beine + k*kanienchen_beine
#         if ergebnis == beine and h +k == köpfe:
#             print(pa, pa2)

# from random import randint
# beine = 94
# köpfe = 35
# huener_beine = 2
# kanienchen_beine = 4
# b = True
# while b == True:
#     x = randint(1, 35)
#     y = randint(1, 35)
#     erg_h = x*huener_beine + y*kanienchen_beine
#     if erg_h == 94 and x +y == 35:
#         print(x, y)
#         b = False

# beine = 114
# köpfe = 26
# huener_beine = 2
# kanienchen_beine = 4
# spinnen_beine = 8
# hüner_schwanz = 1
# kanienchen_schwanz = 1
# for h in range(26):
#     for k in range(26):
#         for s in range(26):
#             pa = h*huener_beine /2
#             pa2 = k*kanienchen_beine /4
#             pa3 = s*spinnen_beine/8
#             ergebnis = h*huener_beine + k*kanienchen_beine + s*spinnen_beine
#             schwänze_anzahl = h*hüner_schwanz + k*kanienchen_schwanz
#             if ergebnis == beine and h +k +s == köpfe and schwänze_anzahl == 19:
#                 print(pa, pa2, pa3)
# p = 0
# for x in range(101):
#     p = x + p
# print(p)
#
# p = 0
# for x in range(-50, 151):
#     if x % 2 == 0:
#         p = p + x 
# print(p)

# p = 0
# for x in range(0, 500):
#     if x % 3 == 0:
#         if x % 7 ==0:
#             p +=1
# print(p)