"""Cuando en un número la diferencia entre cada par de dígitos consecutivos es uno,
se lo llama número "step" (como el 123234, el 9876787654, etc.).
¿Cuántos números "step" menores a un millón existen? Resultado: 458 0 448 creo que es mejor"""

lista=list(range(0,1000000))
lista3=[]

for i in range(10,1000000):
    c= str(lista[i])
    d=len(c)
    lista2=[]
    for e in range(0,d-1):
        f=int(c[e])-int(c[e+1])
        if f==1 or f==-1:
            lista2.append(int(e))
        else:
            continue
    g=len(lista2)    
    if (d-1)==g:
        lista3.append(lista[i])
    else:
        continue
    
print((lista3))
print(len(lista3))