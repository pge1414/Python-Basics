import random
#listen ermöglchen es mehrere werte in einger variable zu speichern

liste1 = [1,2, 3]
liste2 = ['haus', 100, True]
liste3 = [1]
liste4 = [[1, -2, -3], "F", "Atlas"]
liste6 = [1,2,3,4,5]
liste3.append(25)
print(liste3)
liste1.remove(2)
print(liste1)
liste1.pop(1)
print(liste1)
liste4.pop()
print(liste4)
liste5 = liste1 + liste2
print(liste5)
element1 = liste2[0]
print(element1)
element2= liste2[2]
print(element2)
element3 = liste2[-1]
print(element3)
liste4[1] = 2.5
print(liste4)
element4= random.choice(liste4)
print(element4)
liste6.pop(0)
print(liste6)
l = len(liste6)
liste4.insert(1, "Ocean")
print(liste4)
element5= liste6[-2]
print(element5)