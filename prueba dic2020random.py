import random


n=0
l=0
for i in range (1,21):
    cadena=[]
    x=random.randint(0,100)
    cadena.append(x)
    while True:
        x=random.randint(0,100)
        cadena.append(x)
        
        if x%2==0 and (x<=60 and x>=40):
            print("Tirada",i,":",cadena)
            if len(cadena)>l:
                n=i
                l=len(cadena)

            break
print("La tirada más larga es la ",n, "con una longitud de",l)


