"""Calcular el día que cae una fecha, posterior a 1582:
   - A es el cociente de la división de 14 menos el mes entre 12,
   - B es el año menos A
   - C es el mes más doce veces A menos 2
   - D es el cociente de la división de B entre 4
   - E es el cociente de la división de B entre 100
   - F es el cociente de la división de B entre 400
   - G es el cociente de 31 veces C entre 12
   - H es el dia más B más D menos E más F más G
   - I es el resto de la división de H entre 7
   - Si I es 0, el día cae en Lunes; si I es 1, el día cae en Martes, etc
   - El programa no tiene por qué comprobar que se escribe una fecha correcta (más allá de que el año sea posterior a 1582)"""
print("Ponga la fecha que desee calcular")
a=input("Año: ")
a=eval(a)
if a<=1582:
    print("La fecha debe ser posterior a 1582")
else: 
    b=input("Mes, en número: ")
    c=input("Día: ")
    b=eval(b)
    c=eval(c)
    lista=["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado","Domingo"]
    A=((14-b)//12)
    B=a-A
    C=b+(12*(A-2))
    D=B//4
    E=B//100
    F=B//400
    G=(31*C)//12
    H=c+B+D-E+F+G
    I=H%7
    print("Esa fecha cae un",lista[I])
