"""Realiza un programa que genere 15 resultados 1, x o 2. Como una apuesta de la quiniela."""
from random import *
lista=[1,"X",2]
a=choices(lista,k=15)
print(a)