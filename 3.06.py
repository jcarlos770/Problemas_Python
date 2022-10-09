"""Si listamos todos los números naturales menores a 10 que son multiplos de 3 o 5, tenemos 3, 5, 6 y 9.
La suma de estos múltiplos es 23.
Encontrar y mostrar la suma de todos los multiplos de 3 o 5 menores a 1000. Resultado: 233168"""

lista=[]
for i in range (1,1000):
    if i%3==0 or i%5==0:
        lista.append(i)
    else:
        continue
b=len(lista)
c=lista[0]
for i in range(1,(b)):
    c=c+lista[i]
print(c)
    