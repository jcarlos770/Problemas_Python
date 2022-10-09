"""Definir una función max() que tome como argumento dos números y devuelva el mayor de ellos.
(Es cierto que python tiene una función
max() incorporada, pero hacerla nosotros mismos es un muy buen ejercicio."""
import random
a=random.randint(0,100)
print(a)
b=random.randint(0,100)
print(b)
c=random.randint(0,100)
print(c)
def mayor(x,y):
    if x==y:
        print("Es el mismo número")
    elif x>y:
        print("El número",x," es mayor que",y)
    else:
        print("El número",y," es mayor que",x)
mayor(a,b)
d=max(a,b)
print(d)
a=2
b=1
c=2
def mayordetres(x,y,z):
    if x==y and x==z:
        print("Los números son iguales")
    elif (x>y or x==y) and (x>z or x==z):
        print("El número mayor es",x)
    elif (y>x or x==y) and (y>z or y==z):
        print("El número mayor es",y)
    elif (z>y or z==y) and (z>x or x==z):
        print("El número mayor es",z)
mayordetres(a,b,c)