#Realizar una programa que solicite una palabra y sólo muestre las vocales de dicha palabra.
a=input("Escribe una palabra: ")
n=0
b=len(a)
consonantes=[]
for n in range (0,b):
    if a[n]!=("a") and a[n]!=("e") and a[n]!=("i") and a[n]!=("o") and a[n]!=("u"):
        consonantes.append(a[n])
    n=n+1
print(consonantes)
    

    