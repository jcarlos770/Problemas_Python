"""Realiza un programa que tenga 10 nombres escritos en una lista, y que elija aleatoriamente
tres de los nombres de la lista. Nota: usa el módulo random y la función sample de este
módulo."""
from random import *
lista=["El","unicornio","azul","ayer","se","me","escapó","quien","sabe","donde"]
nom=sample(lista,3)
print (nom)