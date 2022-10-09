"""3.03. Hacer un programa que le pida una cadena al usuario, y arme una triángulo creciente y decreciente con ese texto. Por ejemplo, para el texto "klop", el resultado sería:
  k
  kl
  klo
  klop
  klo
  kl
  k"""

a=input("Inserta un texto")
b=len(a)
for i in range(0,b):
     print(a[0:i])
for i in range(b,0,-1):
     print(a[0:i])