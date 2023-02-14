#eine funktion die die fakultät von n berechnet und zurückgibt ohne dass dabei schleifen verwendet werden
from importlib.resources import read_text
from lib2to3.pytree import NegatedPattern
from re import I
from turtle import rt


# def fak(n : int) -> int:
#     if n == 0:
#         return 1
#     fak_vorgänger =  fak(n - 1)
#     fak_n = n * fak_vorgänger
#     return fak_n
# print(fak(4))
#eine funktion die die quersumme von n berechnet und zurückgibt, ohne dass dabei schleifen verwendet werden
#hier werden string methoden verwendet
# def quersumme_string(n : int) -> int:
#     n_str = str(n)
#     if len(n_str) == 1:
#         return n
#     quersumme_alt = int(n_str[1:])
#     quersumme_vorgänger = quersumme_string(quersumme_alt)
#     quersumme = int[n_str[0]] + quersumme_vorgänger
#     return quersumme
# print(quersumme_string(46))

#hier werden keine string methoden verwendet, dafür die arithmethischen operatoren % steht für modulo // für integer division
# def quersumme_arithmethisch(n : int) -> int:
#     c_alt = 0
#     c = n % 10
#     n =  n // 10
#     c_alt = c + c_alt
#     if len(str(n)) == 0:
#         return c_alt


# print(quersumme_arithmethisch(114))


#eine funktion die true zurückgibt falls ein wort ein palindrom ist
# def palindrom(wort: str) -> bool:
#     stellen = len(wort)
#     wort_stelle = palindrom(str(wort_stelle) + str(wort[stellen-1]))
#     if stellen == 0:
#         if wort == wort_stelle: 
#             return 1 
#         else: 
#             return 0

# print(palindrom("dkdk"))

def fib(o: int)-> int:
    if o == 0:
        return 0
    if o == 1:
        return 1
    return fib(o-1)+fib(o-2)

    

print(fib(8))
