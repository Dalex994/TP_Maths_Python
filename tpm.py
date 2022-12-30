import matplotlib.pyplot as plt
import numpy as np

def f(t):
    return 2/(1+t)

a=0
b=10
n=20
h= (b-a)/n

abs=[a+i*h for i in range (n+1)]
ord= [f(t) for t in abs]
plt.plot(abs,ord, 'b')
plt.show()

def Liste(x,y,range_b,L,dir_coeffs):
    L = []
    ecart_b = range(0, b)
    x = np.array()
    y = np.array()

    for i in ecart_b:
        i = i+2


    dir_coeffs = np.gradient(y, x)

    L.append(dir_coeffs)

    show(L)
