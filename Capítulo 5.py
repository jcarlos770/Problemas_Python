from random import *
from math import *
import pandas
print('Este programa calculará las raíz cuadrada,')
print('de los números: 1 al 10')
for x in range(1,11):
    print(x,sqrt(x))
print('Este programa realiza la suma de un conjunto de valores')
valores=(2,4,12,5,31,45,32,13,15)
print(valores)
suma=fsum(valores)
print('La suma de los números es',suma)