"""Listar los números entre 1 y 10. En la columna contigua sus cuadrados, y en la tercera columna sus cubos.
Al final dar la suma de todos los valores de cada columna."""
for x in range (1,11):
    y=x**2
    z=x**3
    k=x+y+z
    print(x,y,z,k)
        