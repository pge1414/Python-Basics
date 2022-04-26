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