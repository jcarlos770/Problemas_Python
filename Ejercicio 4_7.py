"""Realizar un programa que solicite un número y muestre todos los divisores de ese número y
además cuente el número de divisores de dicho número.
Nota: Aplicar el concepto de contador, contador=contador+1 cada vez que se encuentre un
divisor."""
print('Programa para conocer los divisores de un número')
a=1
while a<2:
    n = input('¿De qué número quieres conocer los divisores?: ')
    n = eval(n)
    lista_1 = []
    lista_2 = []
    i=1
    while i<=n:
        lista_1.append(i)
        i=i+1
    c=1
    for i in range (1,n):
        if ((n%(lista_1[c]))==0):
            lista_2.append(c)
            c=c+1
        else:
            c=c+1
    print("Tiene",(len(lista_2)),"divisores")
    print("Los divisores son: ",lista_2)
        
        

    a=a+1
    ask=input("¿Quieres buscar los divisores de otro número (Y/N)?")
    if ask == ("Y"):
        a=1
    else:
        a=a