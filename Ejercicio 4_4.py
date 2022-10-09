#Realizar una programa que solicite una palabra y sólo muestre las vocales de dicha palabra.
a=input("Escribe una palabra: ")
n=0
b=len(a)
vocales=[]
for n in range (0,b):
    if a[n]==("a"):
        vocales.append(a[n])
    if a[n]==("e"):
        vocales.append(a[n])
    if a[n]== ("i"):
        vocales.append(a[n])
    if a[n]== ("o"):
        vocales.append(a[n])
    if a[n]== ("u"):
        vocales.append(a[n])
    n=n+1
print(vocales)
    

    