from matplotlib import pyplot
import math
import random
lista=[]
punto=[]
for i in range (0,10):
    a=random.randint(0,10)
    b=random.randint(0,10)
    punto.append(a)
    punto.append(b)
    lista.append(punto[i])

pyplot.plot(lista,"bo")

pyplot.show()