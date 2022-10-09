from random import *
print("En este juego deberás buscar un número entre cero y 100 en el menor número de intentos posibles")
a=randint(0,100)
b=a-1
n=1
while (b!=a):
    b=input("Adivina el número: ")
    b=eval(b)
    if b>a:
        print("El número es menor")
        n=n+1
    if b<a:
        print("El número es mayor")
        n=n+1
    if b==a:
        print("Haz acertado en",n,"intentos")
        c=input("¿Quieres volver a jugar?(Y/N)")
        if c==("Y"):
            a=randint(0,100)
            n=1
            continue
        else:
            break
            



            