eingabe = input()
index = 0
l = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]

def verschlüsseln(eingabe: str) -> str:
    eingabe = eingabe.upper()
    text_v = ""
    index = 0
    if eingabe in l:
        while index <len(eingabe):
            if eingabe[index] == "A":
                text_v = text_v + "F"
            elif eingabe[index] == "B":
                text_v = text_v + "g"
            elif eingabe[index] == "C":
                text_v = text_v + "h"
            elif eingabe[index] == "D":
                text_v = text_v + "i"
            elif eingabe[index] == "E":
                text_v = text_v + "j"
            elif eingabe[index] == "F":
                text_v = text_v + "k"
            elif eingabe[index] == "G":
                text_v = text_v + "l"
            elif eingabe[index] == "H":
                text_v = text_v + "m"
            elif eingabe[index] == "I":
                text_v = text_v + "n"
            elif eingabe[index] == "J":
                text_v = text_v + "o"
            elif eingabe[index] == "K":
                text_v = text_v + "p"
            elif eingabe[index] == "L":
                text_v = text_v + "q"
            elif eingabe[index] == "M":
                text_v = text_v + "r"
            elif eingabe[index] == "N":
                text_v = text_v + "s"
            elif eingabe[index] == "O":
                text_v = text_v + "gu"
            elif eingabe[index] == "P":
                text_v = text_v + "gw"
            elif eingabe[index] == "Q":
                text_v = text_v + "gx"
            elif eingabe[index] == "R":
                text_v = text_v + "gy"
            elif eingabe[index] == "S":
                text_v = text_v + "gz"
            elif eingabe[index] == "T":
                text_v = text_v + "g1"
            elif eingabe[index] == "U":
                text_v = text_v + "g2"
            elif eingabe[index] == "V":
                text_v = text_v + "g3"
            elif eingabe[index] == "W":
                text_v = text_v + "g4"
            elif eingabe[index] == "X":
                text_v = text_v + "g5"
            elif eingabe[index] == "Y":
                text_v = text_v + "g6"
            elif eingabe[index] == "Z":
                text_v = text_v + "g7"
                
            index = index +1
        return text_v
    else:
        print(eingabe)

