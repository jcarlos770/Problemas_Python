#Tabla de multiplicar
a=int(input ("¿Qué tabla quieres que ponga?"))
lista=[]
listar=[]
for e in range (1,11):
    lista.append(e)
    e=e+1
for i in range (0,10):
    listar.append(a*lista[i])
    i=i+1
print(listar)