"""Indicar las dimensiones de los triángulos rectángulos donde todas sus longitudes sean números enteros.
 Listarlos hasta el límite donde los catetos lleguen hasta 100.
 3 4 5
5 12 13
6 8 10
7 24 25
8 15 17
9 12 15
9 40 41
10 24 26
11 60 61
12 16 20
12 35 37
13 84 85
14 48 50
15 20 25
15 36 39
16 30 34
16 63 65
18 24 30
18 80 82
20 21 29
20 48 52
20 99 101
21 28 35
21 72 75
24 32 40
24 45 51
24 70 74
25 60 65
27 36 45
28 45 53
28 96 100
30 40 50
30 72 78
32 60 68
33 44 55
33 56 65
35 84 91
36 48 60
36 77 85
39 52 65
39 80 89
40 42 58
40 75 85
40 96 104
42 56 70
45 60 75
48 55 73
48 64 80
48 90 102
51 68 85
54 72 90
56 90 106
57 76 95
60 63 87
60 80 100
60 91 109
63 84 105
65 72 97
66 88 110
69 92 115
72 96 120
75 100 125
80 84 116    """ 
"""import math
x=1
y=1
for x in range (1,101):
    for y in range (1,101):
        h=math.sqrt(x**2+y**2)
        k=h//1
        if k==h:
            print(x,y,int(h))
            y=y+1
        else:
            y=y+1
    x=x+1               """

import math
x=1
y=1
for x in range (1,101):
    for y in range (1,101):
        h=math.sqrt(x**2+y**2)
        k=int(h)
        if k==h:
            print (x,y,k)

            
