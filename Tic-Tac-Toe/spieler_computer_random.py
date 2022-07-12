import random


class Spieler_Computer_Random:
    def __init__(self, name):
        self.name = name
        self.symbol = None

    def zug(self,spielfeld,platz):
        gültige_eingabe = False
        while not gültige_eingabe:
            feld = random.choice(spielfeld)
            if feld in spielfeld and feld != 'x' and feld != 'o':
                gültige_eingabe = True
            else:
                gültige_eingabe = False
        return feld