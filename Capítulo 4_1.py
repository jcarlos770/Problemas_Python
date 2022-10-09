print('Este programa deletrea una palabra,')
print('escribe cada uno de sus caracteres y el valor unicode del carácter')
n=1
while n<2:
    palabra=input('Escribe una palabra: ')
    for c in palabra:
        print(c,'valor unicode:',ord(c),'\n')
    n=n+1
    d= input ("¿Quieres probar otra vez (Y/N)?")
    if d==("Y"):
        n=1
    else:
        n=n