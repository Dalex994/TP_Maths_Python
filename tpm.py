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

def Liste(x,y,n):
    L = []
    x = np.array()
    y = np.array()

    dir_coeffs = np.gradient(y, x)

    L.append(dir_coeffs)
    show(L)
