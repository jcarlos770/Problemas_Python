"""Imprimir una lista de 10 números aleatorios sin repetición que varíen en el rango 80 a 99.
Volver a imprimir la lista pero ordenada."""
import random
Lista=[random.randint(80,99)]
i=1
while i<10:
    x=random.randint(80,99)
    if x not in Lista:
        Lista.append(x)
        i=i+1
    else:
        continue
print (Lista)
print(sorted(Lista))