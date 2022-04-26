
# Bibt True zurück, falls Zahl gerade ist ansonsten false
# def gerade(zahl: int) -> bool:
#     if zahl % 2 == 0:
#         return True
#     else:
#         return False

# print(gerade(5))

# Gibt die größere der beiden Zahlen zurück, falls Zahl gerade ist ansonsten

# def größere(zahl1: int, zahl2: int) -> int:
#     if zahl1 < zahl2:
#         return zahl2
#     if zahl1 > zahl2:
#         return zahl1
#     else:
#         print("Zahlen sind gleich groß")
#         return
# print(größere(2,4))
def großte(zahl1: int, zahl2: int, zahl3: int) -> int:
    if zahl1 > zahl2 and zahl1 > zahl3:
        return zahl1
    if zahl2 > zahl1 and zahl2 > zahl3:
        return zahl2
    if zahl3 > zahl2 and zahl3 > zahl1:
        return zahl3
    else:
        return("Geht nicht")
print(großte(zahl1=2, zahl2=2, zahl3=3))
