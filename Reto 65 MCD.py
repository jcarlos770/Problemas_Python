"""Máximo Común Divisor
Programar el algoritmo de Euclides para calcular el MCD (Máximo Común Divisor)."""
import math

a=input("Introduce tu primer número: ")
b=input("Introduce tu segundo número: ")
a=int(a)
b=int(b)
lista1=[]
lista2=[]
for i in range(1,(a+1)):
    c=a%i
    if c==0:
        lista1.append(i)
    else:
        continue
for e in range(1,(b+1)):
    c=b%e
    if c==0:
        lista2.append(e)
    else:
        continue
print("Divisores de ", a,":",lista1)
print("Divisores de ", b,":",lista2)
lista_final = []
for i in lista1:
    if (i not in lista_final) and (i in lista2):
        lista_final.append(i)

print("Divisores comunes de ",a," y ",b, " :", lista_final)
print("El MCD de ",a," y ",b,"es : ",max(lista_final))