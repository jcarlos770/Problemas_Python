"""Pedir al usuario un número entero, y mostrar la lista de 1 a ese número, junto con el correspondiente factorial. Por ejemplo, si el usuario ingresa 4 (prestar atención a lo prolijo del encolumnado):
  1  1
  2  2
  3  6
  4 24"""

a=input("Introduzca un número ")
a=int(a)
c=1
for i in range (0,(a)):
    c=c*(i+1)
    print((i+1),"! =",c)

    


