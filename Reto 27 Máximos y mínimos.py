"""Generar 10 números aleatorios y calcular el máximo y el mínimo."""
from numpy import random
x1=int(random.random()*100)
x2=int(random.random()*100)
x3=int(random.random()*100)
x4=int(random.random()*100)
x5=int(random.random()*100)
x6=int(random.random()*100)
x7=int(random.random()*100)
x8=int(random.random()*100)
x9=int(random.random()*100)
x10=int(random.random()*100)
lista=[x1,x2,x3,x4,x5,x6,x7,x8,x9,x10]
"""print (lista)"""
maximo=max(lista)
minimo=min(lista)
print("La lista de números es la siguiente",lista)
print("El número mayor es...",maximo)
print("El número menor es...",minimo)