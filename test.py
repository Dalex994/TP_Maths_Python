import matplotlib.pyplot as plt
import numpy as np


def f(t):
    return 2/(1+t)

a = 0
b = 10
n = 20
h = (b-a)/n

abs = [a+i*h for i in range(n+1)]
ord = [f(t) for t in abs]

def Liste(L,x,y,range_b,dir_coeffs):


    for range_b in range(0, b):
        L = []
        b2 = range_b+2
        x = abs+b2
        y = (f(t) for t in x)
        dir_coeffs = np.gradient(y, x)
        L.append(dir_coeffs)
        print("Values from the directing coefficients of secants to the curve are {0}".format(len(L)))
