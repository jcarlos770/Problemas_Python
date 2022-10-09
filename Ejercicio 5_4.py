"""Realiza un programa que solicite una palabra y a continuación muestre un carácter aleatorio de
los que contenga la palabra introducida."""
from random import *
a=input("Escribe una palabra: ")
b=len(a)
c=randint(0,b)
print("Este carácter pertenece a tu palabra:",(a[c]))