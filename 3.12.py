""" Un número palíndromo se lee igual en los dos sentidos. El palíndromo más grande formado del producto
de números de dos dígitos es 9009 (91 x 99).
Encontrar el palíndromo más grande
formado por el producto de dos números de tres dígitos.
Resultado: 906609 (993 * 913)"""
lista=[]
listaX=[]
listaY=[]
lista2=[]
for i in range(0,1000):
    lista.append(i)
for e in range (0,1000):
    X=int(lista[e])
    for f in range(0,1000):
        Y=int(lista[f])
        Z=str(X*Y)
        if Z==Z[::-1]:
            lista2.append(int(Z))
            listaX.append(X)
            listaY.append(Y)
        else:
            continue
b=int(max(lista2))
c=lista2.index(b)
print(lista2[c],listaX[c],listaY[c])