"""Realizar un programa que solicite una palabra, genere una lista a partir de dicha palabra y
muestre la lista."""
a=input("Dí una palabra: ")
deletrear=[]
b=len(a)
for i in range (0,b):
    deletrear.append(a[i])
    i=i+1
print(deletrear)