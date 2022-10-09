"""Se escriben todos los números enteros positivos en una lista,
ordenados y empezando por el 1 (en la posición 0),
luego se tachan todos los que tienen el dígito 9 al
menos una vez, y después se tachan todos los múltiplos de 3.
Considerando solamente los números no tachados,
¿qué número queda en la posición un millón? Resultado: 2735546"""

lista=[]
for i in range(1,10000000):
    if "9" in str(i) or i%3==0:
        continue
    else:
        lista.append(i)
print(lista[1000000])
    