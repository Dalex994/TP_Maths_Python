import matplotlib.pyplot as plt

def f(t):
    return 2/(1+t)

a=0
b=10
n=30
h= (b-a)/n
def coeffs_dirr(pas):
    ret = []
    i = 0.5
    while i<10:
        ret.append((f(i+0.001)-f(i))/0.001)
        i+= pas
    return ret

abs=[a+i*h for i in range(n+1)]
ord= [f(t) for t in abs]
print(coeffs_dirr(1 ))
plt.plot(abs,ord, 'b')
plt.show()
