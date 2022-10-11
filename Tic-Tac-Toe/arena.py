from spieler_mensch import Spieler_Mensch
from spieler_computer_random import Spieler_Computer_Random
from spieler_computer_schlau import Spieler_Computer_Schlau
import random

class Arena:
    def __init__(self):
        self.spielfeld = []
        

    def __ausgabe(self):
        print(" " + self.spielfeld[0] + " | " + self.spielfeld[1] + " | " + self.spielfeld[2])
        print("-----------")
        print(" " + self.spielfeld[3] + " | " + self.spielfeld[4] + " | " + self.spielfeld[5])
        print("-----------")
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
            spieler1.symbol = "o"


        spiel_fertig = False

        while not spiel_fertig:

            feld = spieler1.zug(self.spielfeld) if spieler == spieler1 else spieler2.zug(self.spielfeld)
            
            
            self.spielfeld[int(feld) - 1 ] = spieler.symbol

            self.__ausgabe()

            if self.__gewinnprüfung():
                print("Du hast gewonnen " + spieler.name)
                spiel_fertig = True

            spieler = spieler2 if spieler == spieler1 else spieler1

# antwort = input("Möchtest du Mensch gegen Mensch oder gegen den Computer spielen?(Computer/Mensch)")

# if antwort == "Computer":

#     antwort_schwierigkeitsgrad = input("Welchen Schwierigkeitsgrad möchtest du wählen?(eazy/impossible)")
#     if antwort_schwierigkeitsgrad == "eazy":
#         a = Arena()
#         s1 = Spieler_Mensch("Spieler 1")
#         s2 = Spieler_Computer_Random("Computer")
#         a.spielen(s1, s2)

#     if antwort_schwierigkeitsgrad == "impossible":
a = Arena()
s1 = Spieler_Mensch("Spieler 1")
s2 = Spieler_Computer_Schlau("Computer")
a.spielen(s1, s2)


# elif antwort == "Mensch":
#     a = Arena()
#     s1 = Spieler_Mensch("Spieler 1")
#     s2 = Spieler_Mensch("Spieler 2")
#     a.spielen(s1, s2)
