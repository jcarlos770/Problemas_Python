import turtle
import random
for i in range(2):
    a=random.randint(10,100)
    b=random.randint(0,90)
    c=random.randint(0,100)
    d=random.randint(0,100)
    turtle.up()
    turtle.ht()
    turtle.goto(c, d)

# reshow the turtle
    turtle.st()
    turtle.down()
    for i in range (2):
        turtle.forward(a)
        turtle.right(90)
        turtle.forward(b)
        turtle.right(90)

