"""Escribir una función mas_larga() que tome una lista de palabras y devuelva la mas larga."""
a=input("¿Cuántas palabras quiere escribir? ")
a=int(a)
lista=[]
for i in range(0,a):
        b=input("Escribe la palabra: ")
        lista.append(b)
def maslarga(x):
    lista2=[]
    for i in range (0,len(x)):
        lista2.append(int(len(x[i])))
        c=max(lista2)
    print("La palabra más larga tiene",c,"caracteres")
maslarga(lista)