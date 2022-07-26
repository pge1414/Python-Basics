import random
class Spieler_Computer_Schlau:
    def __init__(self,name):
        self.name = name
        self.symbol = None
        self.symbol_gegner = None

    def __gewinnprüfung(self):
        return self.spielfeld[0] == self.spielfeld[1] == self.spielfeld[2] or \
                self.spielfeld[3] == self.spielfeld[4] == self.spielfeld[5] or \
                self.spielfeld[6] == self.spielfeld[7] == self.spielfeld[8] or \
                self.spielfeld[0] == self.spielfeld[3] == self.spielfeld[6] or \
                self.spielfeld[1] == self.spielfeld[4] == self.spielfeld[7] or \
                self.spielfeld[2] == self.spielfeld[5] == self.spielfeld[8] or \
                self.spielfeld[0] == self.spielfeld[4] == self.spielfeld[8] or \
                self.spielfeld[2] == self.spielfeld[4] == self.spielfeld[6]

    def __freie_felder(self, spielfeld):
        return [freies_feld for freies_feld in spielfeld if freies_feld not in ["x", "o"]]

    def __bewertung(self, spielfeld,symbol):
        if symbol == self.symbol:
            if self.__gewinnprüfung(spielfeld):
                return -(len(self.__freie_felder(spielfeld))+1)
            if len(self.__freie_felder(spielfeld)) == 0:
                return 0
            max = -1
            for freies_feld in self.__freie_felder(spielfeld):
                spielfeld[int(freies_feld) - 1] = self.symbol
                bewertung = self.__bewertung(spielfeld, symbol_gegner)
                if bewertung > max:
                    max = bewertung