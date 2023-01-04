#Este programa va a calcular los n primeros terminos de una progresion aritmetca
a=input("¿Cual es el primer termino de la progresion?")
a=int(a)
b=input("¿Cual esla diferencia de la progresionaritmetica?")
b=int(b)
c=input("¿Cuantos terminos quieres conocer ?")
c=int(c)
lista=[]
for i in range(1,c+1):
	d=a+(i-1)*b
	lista.append(d)
print(lista)

