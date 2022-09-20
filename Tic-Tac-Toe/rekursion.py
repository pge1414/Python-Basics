#eine funktion die die fakultät von n berechnet und zurückgibt ohne dass dabei schleifen verwendet werden
from lib2to3.pytree import NegatedPattern


# def fak(n : int) -> int:
#     if n == 0:
#         return 1
#     fak_vorgänger =  fak(n - 1)
#     fak_n = n * fak_vorgänger
#     return fak_n
# print(fak(4))
#eine funktion die die quersumme von n berechnet und zurückgibt, ohne dass dabei schleifen verwendet werden
#hier werden string methoden verwendet
def quersumme_string(n : int) -> int:
    n_str = str(n)
    if len(n_str) == 1:
        return n
    quersumme_alt = int(n_str[1:])
    quersumme_vorgänger = quersumme_string(quersumme_alt)
    quersumme = int[n_str[0]] + quersumme_vorgänger
    return quersumme
print(quersumme_string(46))

#hier werden keine string methoden verwendet, dafür die arithmethischen operatoren % steht für modulo // für integer division
def quersumme_arithmethisch(n : int) -> int:
    pass

#eine funktion die true zurückgibt falls ein wort ein palindrom ist
def palindrom(wort: str) -> bool:
    pass

