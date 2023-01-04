#Este programa va a calcular los n primeros terminos de una progresion geometrica
a=input("¿Cual es el primer termino de la progresion?")
a=int(a)
b=input("¿Cual es la razon de la progresion geometrica?")
b=int(b)
c=input("¿Cuantos terminos quieres conocer ?")
c=int(c)
lista=[]
for i in range(1,c+1):
	d=a*(b**(i-1))
	lista.append(d)
print(lista)

