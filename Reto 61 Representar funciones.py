"""Representar funciones
Representar gráficamente el polinomio y=x^4-3x^2+2."""

import matplotlib
from matplotlib import pyplot

# Función bicuadrática.
def f1(x):
    return (x**4)-(3*x**2)+2
# Valores del eje X que toma el gráfico.
x=range(-15,15)
# Graficar la función.
pyplot.plot(x, [f1(i) for i in x])

pyplot.show()