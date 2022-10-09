"""Cada tirada genera una sucesión de números aleatorios entre 1 y 100.
La tirada finaliza cuando se obtiene un número par, entre 40 y 60.
El juego lanza 20 tiradas y al final se dice que tirada ha sido la más larga."""

import random
maxi=0
tirmax='' #texto que recoge la tirada o tiradas de longitud máxima
for i in range(1,21): #generamos las tiradas 1 a 20
  texto='' #cadena que recoge los valores numéricos de una tirada
  n=1 #número de elementos que tiene cada tirada
  while True:
    x=random.randint(1,100) #aleatorio entero entre 1 y 100
    texto=texto+str(x)+' ' #añadimos a la frase un nuevo elemento y un espacio
    if x%2==0 and 40<=x<=60: #cuando se ha de detener la generación de números en cada tirada
      print('Tirada',i,':',texto) #se imprime la frase de la tirada i-ésima
      if n>maxi: #si el nº de elemento de esta tirada (n) es mayor que el máximo que existía hasta ahora
        maxi=n #nuevo máximo
        tirmax=str(i)+','+' ' #si tenemos nuevo máximo la frase tirmax se inicializa con el indice de la tirada actual
      elif n==maxi: #si el nº de elemento de la tirada es igual al máximo actual
        tirmax+=str(i)+','+' ' #la frase tirmax añade el indice de la tirada actual
      break #nos salimos del bucle while porque ya se ha cumplido la condición del if
    n=n+1 #contador: un nuevo elemento dentro de la tirada en la que estamos
print('El maximo nº de elementos ha sido ',maxi,' y se alcanza en ',tirmax[:len(tirmax)-2]+'.')
#al final se imprime tirmax pero se quita la última coma y se añade al final un punto.
