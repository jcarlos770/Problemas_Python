i=1
while i<2:
    a=input("Escribe un número: ")
    b=input("Escribe otro número: ")
    n=float(a)
    m=float(b)
    s=n*m
    print("La multiplicación de los dos números es:",s)
    i=i+1
    ask=input("¿Quieres seguir haciendo multiplicaciones(Y/N)?")
    if ask == ("Y"):
        i=1
    else:
        i=i