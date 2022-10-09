"""Generar cuadrados latinos de tamaño n×n."""
import numpy as np
a=input("Pon el tamaño del cuadrado latino ")
a=int(a)
b=np.arange(a)
print(b)
for i in range(1,a):
    i=np.roll(b,-i)
    print(i)


 