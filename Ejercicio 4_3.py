print('Programa para conocer los divisores de un número')
a=1
while a<2:
    n = input('¿De qué número quieres conocer los divisores?: ')
    n = eval(n)
    lista_1 = []
    i=1
    while i<=n:
        lista_1.append(i)
        i=i+1
    c=0
    for i in range (1,n):
        if ((n%(lista_1[c]))==0):
            print ("Es divisible por",lista_1[c])
            c=c+1
        else:
            c=c+1
        

    a=a+1
    ask=input("¿Quieres buscar los divisores de otro número (Y/N)?")
    if ask == ("Y"):
        a=1
    else:
        a=a