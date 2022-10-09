"""Encontrar dos números X e Y enteros,
mayores o iguales que 2, tales que XY + YX = 94932
(eso es concatenando los dígitos de X e Y, no multiplicando). Resultado: X: 57 Y: 375"""

lista=[]
for i in range(0,1000):
    lista.append(i)
for e in range (0,1000):
    X=str(lista[e])
    for f in range(0,1000):
        Y=str(lista[f])
        c=int(X+Y)
        d=int(Y+X)
        if (c+d)==94932:
            print(X,Y)
        else:
            continue