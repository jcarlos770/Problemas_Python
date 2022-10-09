"""Escriba un programa que calcule el primer dígito de control de una cuenta bancaria,
el que corresponde al código de entidad y oficina.

Las cuatro cifras del código de entidad se multiplican, de izquierda a derecha, por 4, 8, 5 y 10, respectivamente.
Las cuatro cifras del número de oficina se multiplican, de izquierda a derecha por 9, 7, 3 y 6, respectivamente.
Se suman los resultados de las multiplicaciones anteriores.
Se divide por 11 y se toma el resto.
El dígito de control es la diferencia entre 11 y el resto anterior. Si el resultado es 10, el dígito de control es 1.
Si el resultado es 11, el dígito de control es 0
Dígitos de control de ejemplo: 0375 1281 => 3; 0038 3676 => 1; 9517 5646 => 0; 8194 7118 => 7"""


print("Ingrese los datos de su cuenta bancaria: ")
a=input("Código entidad: ")
a=str(a)
lista1=[4,8,5,10]
b=input("Número de oficina")
b=str(b)
lista2=[9,7,3,6]
lista=[]
e=0
for i in range(0,4):
    c=(int(a[i]))*(lista1[i])
    d=(int(b[i]))*(lista2[i])
    e=e+c+d
    i=i+1
f=e%11
g=11-f
if g==11:
    g=0
    
print("El dígito de control es ",g)