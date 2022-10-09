"""Escribir una función sum() y una función multip() que sumen y multipliquen respectivamente
todos los números de una lista. Por ejemplo: sum([1,2,3,4])
debería devolver 10 y multip([1,2,3,4]) debería devolver 24."""
a=input("Escribe un número")

def sum(x):
    c=0
    for i in range(0,len(x)):
        c=c+int(x[i])
    print("La suma de sus cifras da",c)
def multip(x):
    d=1
    for i in range(0,len(x)):
        d=d*int(x[i])
    print("La multiplicación de sus cifras da",d)
    
sum(a)
multip(a)