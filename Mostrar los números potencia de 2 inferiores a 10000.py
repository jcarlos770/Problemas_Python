"""3.01. Mostrar los números potencia de 2 menores a 10000 de la siguiente manera:
  0001
  0002
  0004
  0008
  ..."""
a=1
b=1
lista=[]
while b<10000:
    print(b)
    lista.append(b)
    b=2**a
    a=a+1
print(lista)