i=1
print ("Este programa te servirá para hacer distintas operaciones")
while i<2:
    a=input("Escribe un número: ")
    b=input("Escribe otro número: ")
    n=float(a)
    m=float(b)
    s=n+m
    r=n-m
    p=n*m
    d=n/m
    de=n//m
    resto=n%m
    print("Las operaciones con el número",n,"y",m, "son las siguientes:")
    print("Suma de",n,"y",m,"es",s)
    print("Resta de",n,"menos",m,"da",r)
    print("Multiplicación de",n,"por",m,"da",p)
    print("División de",n,"entre",m,"da",d)
    print("División entera de",n,"entre",m,"da",de)
    print("Resto de la división entera de",n,"entre",m,"da",resto)
    i=i+1
    ask=input("¿Quieres seguir haciendo operaciones (Y/N)?")
    if ask == ("Y"):
        i=1
    else:
        i=i