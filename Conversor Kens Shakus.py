"""Escriba un programa conversor de centímetros a kens y shakus, unidades japonesas de longitud.
Se recuerda que un ken son seis shakus y que un shaku equivale a 30,3 cm.
Si se pone un número no positivo, el programa debe dar un aviso de error.
Escriba el resultado de shakus con dos decimales."""

a=input("Pon la cifra en cm que quieras convertir ")
a=eval(a)
c=0
if a<0:
    print("Error, el número debe ser positivo")
else:
    b=a/(30.3)
    if b>6:
        c=b//6
        d=b%6
        print (round(c,0),"ken y ",round(d,2),"shakus")
    else:
        print(round(b,2), "shakus")