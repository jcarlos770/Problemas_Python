"""Construir una lista que contenga el código de 6 aeropuertos internacionales: MAD, JFK, LHR, CDG, AMS, FRA.
Generar un dado de seis caras, con las siguientes probabilidades 25%, 22%, 18%, 14%, 11%, 10%,
que corresponden a cada uno de los aeropuertos respectivamente.
Generar un listado de 100 aeropuertos extraídos entre los seis del array y que aparezcan de forma aleatoria cada uno
según su probabilidad.
Finalmente mostramos los aeropuertos y el número de veces que aparece cada uno de ellos."""

import random
import numpy as np
random.seed()
L=['MAD','JFK','LHR','CDG','AMS','FRA']
P=[.25,.22,.18,.14,.11,.10]
C=['Madrid','New York','London','Paris','Amsterdam','Frankfurt']
F=[0]*6 #frecuencia de cada aeropuerto
print(L)
print('probabilidad:',P)
A=np.cumsum(P) #acumulado
print('acumulada: ',A)
def intervalo(r,A):
  for i in range(len(A)):
    if r<=A[i]:
      return(i)
for j in range(100):
  r=random.random()
  z=intervalo(r,A)
  F[z]+=1
  print(L[z])
print('--- F R E C U E N C I A S ---')
for k in range(6):
  print(F[k],L[k],C[k])