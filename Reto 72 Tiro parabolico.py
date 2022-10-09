"""Crear un Canvas para ilustrar el tiro parabólico calculando
la distancia alcanzada en función del ángulo α y la velocidad inicial."""

import matplotlib
from matplotlib import pyplot
import math




a=input("Ángulo= ")
b=input("Velocidad inicial= ")
a=float(a)
b=float(b)

"""x=v0·cosθ·t
y=v0·senθ·t-gt2/2"""

def f1(x):
    return b*(math.tan(a))*x-((9.8/((b**2)*(math.cos(a))**2)*x**2))

# Valores del eje X que toma el gráfico.
x = range(0,25)

# Graficar la función.
pyplot.plot(x, [f1(i) for i in x])

pyplot.show()
