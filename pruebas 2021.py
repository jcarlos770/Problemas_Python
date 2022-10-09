from playsound import playsound
a=input("¿Cómo te llamas?")
print("Hola",a)
a=str(a)
c=len(a)
lista=[]
for i in range (0,c):
    lista.append(a[i])
    i=i+1
print(lista)
playsound("2.mp3")