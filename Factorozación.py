"""Pedir al usuario un número entero, y mostrar la lista de 1 a ese número, junto con el correspondiente factorial. Por ejemplo, si el usuario ingresa 4 (prestar atención a lo prolijo del encolumnado):
  1  1
  2  2
  3  6
  4 24"""

def factorizar(b):
    lista=[]
    for i in range(1,b+1):
        c=b%i
        if c==0:
            lista.append(i)
        else:
            continue
    print(lista)
a=input("Escriba un número ")
a=int(a)

for e in range(1,(a+1)):
    d=factorizar (e)

