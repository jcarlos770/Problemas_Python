print('Escribe números pares')
print('Un número impar servirá para terminar')
seguir=True
while seguir:
    numero=input('Escribe un número: ')
    numero=eval(numero)
    if numero%2==1:
        seguir=False