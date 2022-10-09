"""Realizar un programa que solicite entradas de texto hasta que se deje una de las entradas de
texto vacía. Las palabras se irán incluyendo en una lista."""
a=input("Escribe una palabra: ")
b=len(a)
lista=[]
while b!=0:
    lista.append(a)
    a=input("Escribe una palabra: ")
    b=len(a)
print(lista)
    

    