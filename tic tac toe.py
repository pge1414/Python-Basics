import random
print("hello player")
spielfeld = ["1","2","3","4","5","6","7", "8","9"]


def ausgabe():
    print(" " + spielfeld[0] + " | " + spielfeld[1] + " | " + spielfeld[2])
    print("---------")
    print(" " + spielfeld[3] + " | " + spielfeld[4] + " | " + spielfeld[5])
    print("---------")
    print(" " + spielfeld[6] + " | " + spielfeld[7] + " | " + spielfeld[8])


def zug_spieler():
    gültige_eingabe = False
    while not gültige_eingabe:
        feld = input("spieler" + spieler + ", Feld eingeben:")
        if feld in spielfeld and feld != "x" and feld != "o":
            gültige_eingabe = True
        else:
            print("Ungültig")
    return feld

def zug_computer():
    gültige_eingabe = False
    while not gültige_eingabe:
        feld = random.choice(spielfeld)
        if feld in spielfeld and feld != 'x' and feld != 'o':
            gültige_eingabe = True
        else:
            gültige_eingabe = False
    return feld


ausgabe()

spieler = "x"
spiel_fertig = False

while not spiel_fertig:

    feld = zug_spieler() if spieler == "x" else zug_computer()
    
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