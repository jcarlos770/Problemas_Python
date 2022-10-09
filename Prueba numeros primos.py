#100 primeros números primos y gráfica

from pylab import *


lista=[1]
print(lista)
for i in range (1,99):
    for e in range ((i+1),(len(lista))):
        b=((lista[e])%(lista[i]))
        if b!=0:
            lista.append(lista[e])
            e=e+1

        else:
            e=e+1
    i=i+1
print(lista)
plot(lista)
show()