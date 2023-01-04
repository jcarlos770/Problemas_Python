#Este programa va a calcular la diferencia, el primer termino y el termino general de una progresion geometrica
a=input("¿Cual es el primer termino que conoces de la progresion?")
a=int(a)
b=input("¿Que posicion ocupa?")
b=int(b)
c=input("¿Cual es el segundo termino que conoces de la progresion?")
c=int(c)
d=input("¿Que posicion ocupa?")
d=int(d)

e=(c/a)**(1/(d-b))
f=a/((b-1)*e)
print("El primer termino es ",f,"La razon es",e, "y el termino general es","An=",f,"*",e,"**(n-1)")

