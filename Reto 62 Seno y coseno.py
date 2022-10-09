"""Representar funciones
Representar gráficamente seno y coseno."""
import math

import matplotlib
from matplotlib import pyplot

# Función bicuadrática.
def f1(x):
    return math.sin(x)
def f2(x):
    return math.cos(x)
# Valores del eje X que toma el gráfico.
x=range(-5,5)
# Graficar la función.
pyplot.plot(x, [f1(i) for i in x])
pyplot.plot(x, [f2(i) for i in x])
pyplot.show()