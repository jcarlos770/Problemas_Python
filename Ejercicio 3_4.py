print('Programa para conocer los divisores de un número')
p=1
while p<2:
    print("Este programa calcula la letra de tu dni")
    a=input("Porn el número de tu DNI: ")
    a=eval(a)
    b=a%23
    lista="TRWAGMYFPDXBNJZSQVHLCKE"
    print (lista[b])
    p=p+1
    ask=input("¿Quieres buscar más letras (Y/N)?")
    if ask == ("Y"):
        p=1
    else:
        p=p