#Este programa va a calcular la diferencia, el primer termino y el termino general de una progresion aritmetica
a=input("¿Cual es el primer termino que conoces de la progresion?")
a=int(a)
b=input("¿Que posicion ocupa?")
b=int(b)
c=input("Cual es el segundo termino que conoces de la progresion?")
c=int(c)
d=input("¿Que posicion ocupa?")
d=int(d)
e=(c-a)/(d-b)
f=a-(e*(b-1))
print("El primer termino es ",f,"La diferencia es",e, "y el termino general es","An=",f,"+","(n-1)*",e)

