"""Escribir una función max_in_list() que tome una lista de números y devuelva el mas grande."""

a=input("Escribe una cadena ")
lista=[0]
def maxinlist(x):
    for i in range (0,len(x)):
        if int(x[i])>lista[0]:
            lista.remove(lista[0])
            lista.append(int(x[i]))
    print("El número mayor es ",lista[0])
maxinlist(a)
print(max(a))
        