"""Realiza un programa que genere 6 números aleatorios entre 1 y 49. Como el juego de la
primitiva."""
from random import *
lista=[]
for i in range (1,50):
    lista.append(i)
a=sample(lista,6)
print(a)    