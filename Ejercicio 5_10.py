"""Realiza un programa que genere 2 número aleatorios entre 1 y 6 simulando el lanzamiento de
2 dados. Debe mostrar los 2 números obtenidos y la suma de dichos números."""
from random import *
lista=[]
for i in range (1,7):
    lista.append(i)
a=choices(lista,k=2)
print(a)
    