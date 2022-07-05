from hhh import Spieler_Mensch
class Arena:
    def __init__(self, spieler_1: Spieler_Mensch, spieler_2: Spieler_Mensch):
        spieler1 = spieler_1
        spieler2 = spieler_2

    def spielen(self, spieler1, spieler2):
        print("hello player")
        spielfeld = ["1","2","3","4","5","6","7", "8","9"]

        def ausgabe():
            print(" " + spielfeld[0] + " | " + spielfeld[1] + " | " + spielfeld[2])
            print("---------")
            print(" " + spielfeld[3] + " | " + spielfeld[4] + " | " + spielfeld[5])
            print("---------")
            print(" " + spielfeld[6] + " | " + spielfeld[7] + " | " + spielfeld[8])


        
        while not spiel_fertig:
 
            feld = spieler1.zug_spieler() if spieler == "x" else spieler2.zug_spieler()
            
            spielfeld[int(feld) - 1 ] = spieler

            ausgabe()

            if (spielfeld[0] == spielfeld[1] == spielfeld[2] == spieler) or \
                (spielfeld[3] == spielfeld[4] == spielfeld[5] == spieler)or \
                (spielfeld[6] == spielfeld[7] == spielfeld[8] == spieler)or \
                (spielfeld[0] == spielfeld[3] == spielfeld[6] == spieler)or \
                (spielfeld[1] == spielfeld[4] == spielfeld[7] == spieler)or \
                (spielfeld[2] == spielfeld[5] == spielfeld[8] == spieler)or \
                (spielfeld[0] == spielfeld[4] == spielfeld[8] == spieler)or \
                (spielfeld[2] == spielfeld[4] == spielfeld[6] == spieler):
                print("Du hast gewonnen " + spieler)
                spiel_fertig = True

            spieler = 'o' if spieler == 'x' else 'x'

a= Arena()
s1 = Spieler_Mensch()
s2 = Spieler_Mensch()
a.spielen(s1, s2)