"""Generar cuadrados latinos de tamaño a×a."""

a=input("Pon el tamaño del cuadrado latino ")
a=int(a)
lista=[]
cuadrado=[]

for i in range(1,a+1):
    lista.append(i)
cuadrado.append(lista)

cuadrado.append(lista)
print(cuadrado[0])
for i in range(1,a):
    cuadrado[i].insert(len(lista),cuadrado[i][0])
    cuadrado[i].remove(cuadrado[i][0])
    cuadrado.append(cuadrado[i])
    print(cuadrado[i])

