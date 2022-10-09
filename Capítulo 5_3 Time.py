from random import *
from time import *

print('Programa que genera 10 nùmeros aleatorios')
for n in range(10):
    numero=randint(1,100)
    print('Generación:',n+1,'Número generado:',numero)
    sleep(1)