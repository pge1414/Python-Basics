


class spieler_mensch:
    def __init__(self, name):
        self.name = name
        self.symbol = None

    def zug(self,spielfeld):
        gültige_eingabe = False
        while not gültige_eingabe:
            feld = input("spieler" + self.name + ", Feld eingeben:")
            if feld in spielfeld and feld != "x" and feld != "o":
                gültige_eingabe = True
            else:
                print("Ungültig")
        return feld