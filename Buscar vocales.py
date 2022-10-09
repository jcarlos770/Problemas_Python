"""Escribir una función que tome un carácter y devuelva
True si es una vocal, de lo contrario devuelve False"""

a=input('Ingrese su cadena de caracteres:')

def que(x):
    for i in range(0,len(a)):
        if a[i]=="a" or a[i]=="e" or a[i]=="i" or a[i]=="o" or a[i]=="u":
            print(a[i],"es una vocal")
        elif a[i]=="0" or a[i]=="1" or a[i]=="2" or a[i]=="3" or a[i]=="4" or a[i]=="5" or a[i]=="6" or a[i]=="7" or a[i]=="8" or a[i]=="9":
            print(a[i],"es un número")
        else:
            print(a[i],"Es un carácter distinto a vocal o número")
que(a)