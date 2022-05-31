import random
class Tier:
    #Konstruktor
    def __init__(self,tierart: str, nahrung: list, fressfeinde: list, gewicht: float, größe: int, farbe: str):
        self.tierart = tierart
        self.nahrung = nahrung
        self.fressfeinde = fressfeinde
        self.gewicht = gewicht
        self.größe = größe
        self.farbe = farbe

    def __str__(self) -> str:
        return "Tierart: " + str(self.tierart) + " Gewicht: " + str(self.gewicht) + " Größe: " + str(self.größe) + " Farbe: " + str(self.farbe)

    def fressen(self) -> float:
        self.gewicht *= 1.1
        return self.gewicht

    def füttern(self, futtergewicht: float) -> float:
        self.gewicht += futtergewicht * 0.5
        return self.gewicht

    #das tier nimmt jeden tag um 1% an gewicht und 0.5% an größe zu    
    def wachsen(self, tage: int) -> None:
        for i in range(tage):
            self.gewicht += self.gewicht * 0.01
            self.größe += self.größe * 0.005


    def junges(self) -> "Tier":
        gewicht_junges = round(random.uniform(self.gewicht * 0.05, self.gewicht * 0.15), 2)
        größe_junges = int(random.uniform(self.größe * 0.25, self.größe * 0.35))
        nahrung_junges = self.nahrung
        tierart_junges = self.tierart
        farbe_junges = self.farbe
        fressfeinde_junges = self.fressfeinde
        junges = Tier(tierart_junges, nahrung_junges, fressfeinde_junges, gewicht_junges, größe_junges, farbe_junges)
        return junges

class Safaripark:
    def __init__(self, name: str, tiere: list, tourpreis: float):
        self.name = name
        self.tiere = tiere
        self.tourpreis = tourpreis
    #gibt die anzahl an tieren zurück
    def anzahl_tiere(self) -> int:
        return len(self.tiere)

    #gibt den preis pro einem tier zurück
    def preis_pro_tier(self) ->float:
        return self.tourpreis / self.anzahl_tiere

    #nimmt tier in den Safaripark auf
    def aufnehmen(self, tier: Tier) -> None:
        self.tiere.append(tier)

    #gibt das gesamtgewicht aller tiere zurück
    def gesamtgewicht(self) -> float:
        for i in range(len(self.tiere)):
            gesamtgewicht_tiere = self.tiere[i].gewicht
            return gesamtgewicht_tiere

    #gibt die anzahl aller tiere zurück
    def anzahl_tierart(self, tierart: str) -> int:
        anzahl_tierart = 0
        for tier in self.tiere:
            if self.tier == tierart:
                anzahl_tierart += 1
        return


    #Gibt das schwerste tier an
    def schwerste(self) -> Tier:
        for i in range(len(self.tiere)):
            for u in range(len(self.tiere)):
                if self.tiere[i].gewicht < self.tiere[u].gewicht:
                    break
        
        return self.tiere[i]

            

    #gibt das gesamtgewicht aller tiere zurück


tier1 = Tier("Löwe", ["Zebra", "Gazelle", "Gnu"], [], 150.0, 150, "gelb")
tier2 = Tier("Zebra", [], ["Löwe"], 300.0, 210, "schwarz-weiß")
tier3 = Tier("Gnu", [], ["Löwe"], 200.0, 190, "schwarz")

# print(tier1.tierart)
# print(tier2.farbe)
# print(tier3.fressen())
# print(tier1.füttern(2.0))
# tier3.wachsen(30)
# print(tier3.gewicht)
tier4 = tier3.junges()
print(tier4)
safaripark = Safaripark('hahahahahh', [tier1, tier2, tier3], 100.00)
print(schwerste(safaripark))