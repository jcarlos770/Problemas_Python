"""La criba de Eratóstenes es un algoritmo que permite hallar todos los números primos menores que un número dado."""

a=input("Dí un número del que quieras hacer la criba ")
b=int (a)
lista=list(range(1,b))
for i in range(1,(b)):
    for e in range(2,(i)):
       c= i % (e)

       if c==0:
           if i in lista:
               lista.remove(i)
           else:
               continue
    
       else:
           continue
print (lista)