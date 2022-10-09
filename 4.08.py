"""Hacer una función que reciba dos palabras y que imprima linea por linea las primeras,
segundas, etc. letras de ambas palabras. Por ejemplo, llamándola con "Hola" y "mundo", el resultado sería:
    H m
    o u
    l n
    a d
      o"""
a=input("Palabra 1: ")
b=input("Palabra 2: ")
c=len(a)
d=len(b)
e=d-c
if e==0 or e>0:
    for i in range (0,d):
        print(a[i-e],b[i])
else:
    for i in range (0,c):
        print(a[i],b[i+e])   
        