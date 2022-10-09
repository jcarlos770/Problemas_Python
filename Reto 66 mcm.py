"""Máximo Común Divisor
Programar el algoritmo de Euclides para calcular el MCD (Máximo Común Divisor)."""
import math

a=input("Introduce tu primer número: ")
b=input("Introduce tu segundo número: ")
a=int(a)
b=int(b)
lista1=[]
lista2=[]
for i in range(1,b+1):
    c=a*i
    lista1.append(c)

for e in range(1,(a+1)):
    d=b*e
    lista2.append(d)

print("Primeros múltiplos de ", a,":",lista1)
print("Primeros múltiplos de ", b,":",lista2)
lista_final = []
for i in lista1:
    if (i not in lista_final) and (i in lista2):
        lista_final.append(i)

print("Algunos múltiplos comunes de ",a," y ",b, " :", lista_final)
print("El mcm de ",a," y ",b,"es : ",min(lista_final))