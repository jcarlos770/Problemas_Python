import turtle
from math import sqrt

side = 100
turn_angle = 90

for i in range(4):
    turtle.forward(side)
    turtle.left(turn_angle)
turtle.left(0.5*turn_angle)
turtle.forward(side*sqrt(2))
turtle.left(1.5*turn_angle)
turtle.forward(side)
turtle.left(1.5*turn_angle)
turtle.forward(side*sqrt(2))

