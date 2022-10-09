"""Realiza un programa que tenga 10 nombres escritos en una lista, y que elija aleatoriamente
uno de los nombres de la lista. Nota: usa el módulo random y la función choice de este
módulo."""
from random import *
lista=["El","unicornio","azul","ayer","se","me","escapó","quien","sabe","donde"]
nom=choice(lista)
print (nom)