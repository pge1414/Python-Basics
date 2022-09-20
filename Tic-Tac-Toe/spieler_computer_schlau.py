
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
        
        # if symbol == self.symbol:
        #     if self.__gewinnprüfung(spielfeld):
        #         return -(len(self.__freie_felder(spielfeld))+1)
        #     if len(self.__freie_felder(spielfeld)) == 0:
        #         for freies_feld in self.freie_felder(spielfeld):
        #             symbol == self.symbol
        #             if self.__gewinnprüfung(spielfeld):
        #                 return -(len(self.__freie_felder(spielfeld))+1)
        #             if len(self.__freie_felder(spielfeld)) == 0:
        #                 for freies_feld in self.freie_felder(spielfeld):
        #                     symbol == self.symbol_gegner
        #                     if self.gewinnprüfung(spielfeld):
        #                         return -(len(self.__freie_felder(spielfeld))+1)
        #                     if len(self.freie_felder(spielfeld))==0:
        #                         return self.symbol == random.choice(self.freie_felder(spielfeld))
        # for freies_feld in self.freie_felder(spielfeld):
        #     freies_feld = self.symbol
        #     bewertung = 0
        #     if self.gewinnprüfung(spielfeld):
        #         return {bewertung: freies_feld}
        #     if not self.gewinnprüfung(spielfeld):
        #         bewertung += 1
        #         freies_feld = self.symbol_gegner
        #         for freies_feld in self.freie_felder(spielfeld):
        #             if self.gewinnprüfung(spielfeld):
        #                 return {bewertung: freies_feld}
        #             if not self.gewinnprüfung(spielfeld):
        #                 bewertung += 1
        #                 freies_feld = self.symbol
        #                 for freies_feld in self.freie_felder(spielfeld):
        #                     if self.gewinnprüfung(spielfeld):
        #                         return {bewertung: freies_feld}
        #                     if not self.gewinnprüfung(spielfeld):
        #                         break

            
                                
                

    def minimax(self, spielfeld):
            # max = -10
            # bestes_feld = None
            # for freies_feld in self.__freie_felder(spielfeld):
            #     spielfeld[int(freies_feld) - 1] = self.symbol
            #     bewertung = self.__bewertung(spielfeld, self.symbol_gegner)
            #     if bewertung > max:
            #         max = bewertung
            #         bestes_feld = freies_feld
            #     spielfeld[int(freies_feld)-1] = freies_feld
            bestes_feld = self.symbol
            return bestes_feld

    def zug(self, spielfeld):
        self.symbol_gegner = "x" if self.symbol == "o" else "o"
        return int(self.minimax(spielfeld))-1

