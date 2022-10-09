import turtle
from math import sqrt

a=100
b=90
for i in range (6):
    turtle.forward(a)
    turtle.right(-1.5*b)
    turtle.forward(a*sqrt(2))

