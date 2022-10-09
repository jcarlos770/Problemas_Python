"""Escribir una función filtrar_palabras() que tome una
lista de palabras y un entero n, y devuelva las palabras que tengan mas de n caracteres."""
a=input("¿Cuántas palabras quiere escribir? ")
a=int(a)
lista=[]
for i in range(0,a):
        b=input("Escribe la palabra: ")
        lista.append(b)
def filtrar_palabras(x):
    b=input("¿Cuántas letras deseas que tenga la palabra más pequeña?")
    b=int(b)
    for i in range (0,len(x)):
        if (len(x[i]))<b:
            x.remove(x[i])

    print(x)
filtrar_palabras(lista)