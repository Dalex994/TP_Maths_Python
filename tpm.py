import matplotlib.pyplot as plt
import numpy as np

def f(t):
    return 2/(1+t)

a=0
b=10
n=20
h= (b-a)/n

abs=[a+i*h for i in range(n+1)]
ord= [f(t) for t in abs]
plt.plot(abs,ord, 'b')
plt.show()

def Liste(x,y,range_b,L,dir_coeffs):
    L = []

    for ecart_b in range(0, b):
        b2= ecart_b+2
        x= abs+b2
        y= [f(t) for t in x]

dir_coeffs = np.gradient(y, x)

L.append(dir_coeffs)

show(L)
