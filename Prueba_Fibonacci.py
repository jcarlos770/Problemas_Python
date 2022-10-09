#100 primeros números de la sucesión de Fibonacci y gráfica

from pylab import *
import matplotlib.pyplot as plt


a=0
b=1
lista=[a,b]
for i in range (0,100):
    c=a+b
    lista.append(c)
    a=b
    b=c
"""print(lista)"""

plot(lista)
show()