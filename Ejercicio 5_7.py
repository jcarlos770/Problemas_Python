"""Realiza un programa que tenga 10 nombres escritos en una lista, y que muestre los nombres
desordenados, es decir, desordenarlos aleatoriamente. Nota: usa el módulo random y la
función shuffle de este módulo."""
from random import *
lista=["El","unicornio","azul","ayer","se","me","escapó","quien","sabe","donde"]
shuffle(lista)
print(lista)