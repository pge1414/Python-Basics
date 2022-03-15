from random import randint
from turtle import position
text = input()
verschiebung = input()
def verschlüsseln(text, verschiebung):
    for buchs in text:
        position = ord(buchs)
        position_neu_neu = (position+13) % 26
        position_neu = position_neu_neu + verschiebung
        buchs_neu = chr(position_neu)
def verschlüsseln_involutorisch(text):
    text_verschlüsselt = ""
    for zeichen in text:
        ascii_pos = ord(zeichen)
        alphabet_pos = ascii_pos - ord("a")
        alphabet_pos_neu = (alphabet_pos+13) % 26
        ascii_pos_neu = alphabet_pos_neu + ord("a")
        zeichen_neu = chr(ascii_pos_neu)

        text_verschlüsselt = text_verschlüsselt + zeichen_neu

    return text_verschlüsselt

verschlüsselter_text = verschlüsseln_involutorisch(text)
print(verschlüsselter_text)
entschlüsselter_text = verschlüsseln_involutorisch(verschlüsselter_text)
print(entschlüsselter_text)