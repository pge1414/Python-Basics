from spieler_mensch import spieler_mensch
import random

class Arena:
    def __init__(self):
        self.spielfeld = []

    def __ausgabe(self):
        print(" " + self.spielfeld[0] + " | " + self.spielfeld[1] + " | " + self.spielfeld[2])
        print("---------")
        print(" " + self.spielfeld[3] + " | " + self.spielfeld[4] + " | " + self.spielfeld[5])
        print("---------")
        print(" " + self.spielfeld[6] + " | " + self.spielfeld[7] + " | " + self.spielfeld[8])

    def __gewinnprüfung(self):
        return self.spielfeld[0] == self.spielfeld[1] == self.spielfeld[2] or \
                self.spielfeld[3] == self.spielfeld[4] == self.spielfeld[5] or \
                self.spielfeld[6] == self.spielfeld[7] == self.spielfeld[8] or \
                self.spielfeld[0] == self.spielfeld[3] == self.spielfeld[6] or \
                self.spielfeld[1] == self.spielfeld[4] == self.spielfeld[7] or \
                self.spielfeld[2] == self.spielfeld[5] == self.spielfeld[8] or \
                self.spielfeld[0] == self.spielfeld[4] == self.spielfeld[8] or \
                self.spielfeld[2] == self.spielfeld[4] == self.spielfeld[6]


    def spielen(self,spieler1, spieler2):
        
        self.spielfeld = ["1","2","3","4","5","6","7", "8","9"]


        spieler = random.choice([spieler1,spieler2])
        if spieler == spieler:
            spieler1.symbol = "x"
            spieler2.symbol = "o"
        else:
            spieler2.symbol = "x"
            spieler1.symbol = "y"


        spiel_fertig = False

        while not spiel_fertig:

            feld = spieler1.zug(self.spielfeld) if spieler == spieler1 else spieler2.zug(self.spielfeld)
            
            
            self.spielfeld[int(feld) - 1 ] = spieler.symbol

            self.__ausgabe()

            if self.__gewinnprüfung():
                print("Du hast gewonnen " + spieler.name)
                spiel_fertig = True

            spieler = spieler2 if spieler == spieler1 else spieler1
            


        
a = Arena()
s1 = spieler_mensch("Murat")
s2 = spieler_mensch("Mehmet")
a.spielen(s1, s2)