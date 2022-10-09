print('Este programa calcula las tablas de multiplicar')
numero=input('Qué tabla de multiplicar quieres calcular: ')
numero=eval(numero)
lista = []
for n in range(1,10):
    lista.append(n*numero)
print(lista)