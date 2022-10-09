"""3.04. Armar un programa que muestre todas las fichas de dominó, sin repetirlas, una por linea:
  1:1
  1:2
  ...
  6:6"""

for i in range (0,7):
    for e in range(0,7):
        print(i,":",e)