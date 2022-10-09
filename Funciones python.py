import numpy as np

a=input("Di un número ")
a=int(a)
d=np.arange(a+1)
f=[]
for i in range(0,a):
    e=np.roll(d,-i)
    f.append(e)
    print(e)
g= np.array(f)
print(g)