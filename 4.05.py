"""Al listar los primeros seis números primos
(2, 3, 5, 7, 11 y 13), podemos ver que el sexto (6°) primo es 13.
Cual es el 1000° número? Resultado: 7919"""

b=10000
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
print (lista[1000])
