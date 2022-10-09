"""Encriptar y desencriptar frases usando la clave MURCIELAGO. Cada letra de la frase
que coincida con alguna letra de la clave se sustituye por un número siguiendo el orden 0123456789."""

def encriptar(y):
  x1=y.replace('M', '0')
  x2=x1.replace('U', '1')
  x3=x2.replace('R', '2')
  x4=x3.replace('C', '3')
  x5=x4.replace('I', '4')
  x6=x5.replace('E', '5')
  x7=x6.replace('L', '6')
  x8=x7.replace('A', '7')
  x9=x8.replace('G', '8')
  x0=x9.replace('O', '9')
  return x0

def desencriptar(p):
  x1=p.replace('0', 'M')
  x2=x1.replace('1', 'U')
  x3=x2.replace('2', 'R')
  x4=x3.replace('3', 'C')
  x5=x4.replace('4', 'I')
  x6=x5.replace('5', 'E')
  x7=x6.replace('6', 'L')
  x8=x7.replace('7', 'A')
  x9=x8.replace('8', 'G')
  x0=x9.replace('9', 'O')
  return x0

y= input("¿Qué frase quieres encriptar?").upper() or 'HOLA'
z=encriptar(y)
print(z)
print(desencriptar(z))