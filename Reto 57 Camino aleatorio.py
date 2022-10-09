"""Camino aleatorio
Representar gráficamente el camino de un borracho. Comprobar si dados n pasos
la distancia que alcanza tiende a la
raiz cuadrada de n que es el valor teórico de esa distancia."""
import turtle
import math
import random
for i in range(0,5000):
    a=random.randint(0,10)
    b=random.randint(0,4)
    if b==0:
        turtle.forward(a)
    if b==1:
        turtle.back(a)
    if b==2:
        turtle.right(a)      
    else:
        turtle.left(a)

