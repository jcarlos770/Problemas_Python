"""Realizar un programa que muestre sólo los números pares comprendidos entre 1 y 1000."""
print("Este programa muestra los número pares hasta l número que decidas")
n=1
while n<2:
    a=input("Hasta qué número quieres llegar: ")
    a=eval(a)
    lista_pares=[]
    i=1
    while i<=a:
        if i%2==0:
            lista_pares.append(i)
        i=i+1
    print(lista_pares)
    n=n+1
    b=input ("¿Desea repetir(Y/N)?")
    if b==("Y"):
        n=1
    else:
        n=n
    