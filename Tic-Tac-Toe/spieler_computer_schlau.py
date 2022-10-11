
import random
class Spieler_Computer_Schlau:
    def __init__(self,name):
        self.name = name
        self.symbol = None
        self.symbol_gegner = None

    def __freie_felder(self, spielfeld):
        return [freies_feld for freies_feld in spielfeld if freies_feld not in ["x", "o"]]

    def __bewertung(self, spielfeld, symbol):
        if symbol == self.symbol:
            if self.__gewinnprüfung(spielfeld):
                return -(len(self.__freie_felder(spielfeld))+1)
            if len(self.__freie_felder(spielfeld)) ==0:
                return 0
            max = -1
            for freies_feld in self.__freie_felder(spielfeld):
                spielfeld[int(freies_feld)-1] = self.symbol
                bewertung = self.__bewertung(spielfeld, self.symbol)
                if bewertung > max:
                    max = bewertung
                spielfeld[int(freies_feld)-1] = freies_feld
            return max
        else:
            if self.__gewinnprüfung(spielfeld):
                return len(self.__freie_felder(spielfeld))+1
            if len(self.__freie_felder(spielfeld)) == 0:
                return 0
            min = 9
            for freies_feld in self.__freie_felder(spielfeld):
                spielfeld[int(freies_feld)-1]
                bewertung = self.bewertung(spielfeld, self.symbol_gegner)
                if bewertung < min:
                    min = bewertung
                spielfeld[int(freies_feld)-1] = freies_feld
            return min
            

        
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
        
        # if symbol == self.symbol:
        #     spielbewertung_gut = 10
        #     spielbewertung_böse = -10
        #     for i in self.__freie_felder(spielfeld):
        #         i == symbol
        #         if self.__gewinnprüfung(spielfeld):
        #             spielbewertung_gut -= 1
        #             return self.__freie_felder(spielfeld)
        # if not symbol == self.symbol:
        #     for integer2 in self.freie_felder(spielfeld):
        #         integer2 == self.symbol_gegner
        #         if self.__gewinnprüfung(spielfeld):
        #             spielbewertung_böse += 1
                    
            # if len(self.__freie_felder(spielfeld)) == 0:
            #     return 0
            # freies_feld = self.__freie_felder(spielfeld)
            # if self.__gewinnprüfung(spielfeld):
            #     return int(len(self.__freie_felder(spielfeld)))
            # if not self.gewinnprüfung(spielfeld):
            #     freies_feld_index = freies_feld.index(self.__freie_felder())
            #     self.__freie_felder(spielfeld).pop(freies_feld_index)
            #     if symbol == self.symbol:
            #         if self.__gewinnprüfung(spielfeld):
            #             return int(-len(self.__freie_felder(spielfeld)))
            #         if not self.gewinnprüfung(spielfeld):
            #             freies_feld_index = freies_feld.index(self.__freie_felder())
            #             self.__freie_felder(spielfeld).pop(freies_feld_index)
            #             return freies_feld




    def minimax(self, spielfeld, symbol):
        max = -10
        bestes_feld = None
        for freies_feld in self.__freie_felder(spielfeld):
            spielfeld[int(freies_feld) - 1] = self.symbol
            bewertung = int(self.__bewertung(spielfeld, self.symbol_gegner))
            if bewertung > max:
                max = int(bewertung)
                bestes_feld = freies_feld
            spielfeld[int(freies_feld)-1] = freies_feld
        bestes_feld = self.symbol
        return bestes_feld

        bestes_feld = self.__bewertung(spielfeld, symbol)
        return bestes_feld
        

    def zug(self, spielfeld):
        self.symbol_gegner = "x" if self.symbol == "o" else "o"
        feld = int(self.__bewertung(spielfeld))-1
        return feld

