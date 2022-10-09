"""Definir una función que calcule la longitud de una lista o una cadena dada.
(Es cierto que python tiene la función len() incorporada,
pero escribirla por nosotros mismos resulta un muy buen ejercicio."""


a=input('Ingrese su cadena de caracteres:')
def longitud(x):
    c=0
    for i in x:
        c=c+1
    print("La cadena tiene",c,"caracteres")
longitud(a) 
print(len(a))