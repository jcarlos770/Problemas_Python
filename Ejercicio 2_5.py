i=1
print ("Este programa te servirá para hacer distintas operaciones")
while i<2:
    a=input("Escribe una palabra: ")
    b=len(a)
    print ("La palabra tiene",b,"letras")
    c=a[0]
    print("La palabra empieza por la letra",c)
    print("La palabra empieza por",a[0:2])
    print("La palabra termina por",a[(b-2):b])
    i=i+1
    ask=input("¿Quieres seguir analizando palabras (Y/N)?")
    if ask == ("Y"):
        i=1
    else:
        i=i