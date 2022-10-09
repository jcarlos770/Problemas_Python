"""Encuentre la cantidad de enteros entre 1 y 107 para los cuales n y n+1 tienen la misma cantidad de
divisores positivos enteros. Por ejemplo, 14 tiene el 1, 2, 7 y 14,
mientras que 15 tiene 1, 3, 5 y 15. Resultado: 16"""

lista3=[]
for i in range(1,107):
    lista1=[]
    lista2=[]
    for e in range(1,i+2):
        c=(i)%e
        d=(i+1)%e
        if c==0:
            lista1.append(e)
        if d==0:
            lista2.append(e)
        else:
            continue
    if len(lista1)==len(lista2):
         lista3.append(i)
         lista3.append(i+1)
print((lista3))
print("Hay",round(len(lista3)/2,0),"parejas de números que tengan el mismo número de divisores enteros positivos.")
lista4=[]
for i in range (0,len(lista3)-1):
    if lista3[i]==lista3[i+1]:
        lista4.append(lista3[i])
print(lista4)