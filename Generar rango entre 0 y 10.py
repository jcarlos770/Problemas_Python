#Generar rango entre 0 y 10
a=0
lista=[]
"""for i in range (0,10):
    print (a);
    a=a+1;
    i=i+1;"""
while a<11:
    lista.append(a)
    a=a+1
print(lista)
numero=input("¿Qué número quieres eliminar?")
number=int(numero)
lista.remove(number)
print (lista)
