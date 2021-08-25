# -*- coding: utf-8 -*-
import scipy.optimize as sc
from scipy.optimize import root_scalar
import matplotlib.pyplot as plt
import numpy as np

ndigitos = [10**-8, 10**-16,10**-32,10**-56] 

def f(x):
    return x**2 +15*np.cos(x)-40
    #return np.e**x - x - 1
    #return np.longdouble(np.cos(x)*np.cos(x) - x**2)
    #return x**3 -2*x**2 + (4/3)*x-(8/27)
    #return x**3- 2*x-5
    #return x**2


x=np.linspace(start=-10, stop=10,num=100)
plt.plot(x,f(x))
plt.grid()
plt.axhline(y=0,linewidth = 2, c='k'  )
plt.axvline(x=0,linewidth = 2 , c = 'k')
plt.show()

raices=set([])

def metodoBrent(intervalo,digitos):
    formato="{:."+str(digitos).split('-')[1]+"f}"
    if (f(intervalo[0]) <0 and f(intervalo[1])>0) or (f(intervalo[0]) >0 and f(intervalo[1])<0) or (f(intervalo[0])==0):
        solu1= root_scalar(f,method= 'brentq', bracket = intervalo)
        raices.add(formato.format(solu1.root))
        print("Metodo de Brent:")
        print("Raiz: ", formato.format(solu1.root))
        print( "Iteraciones",solu1.iterations )
        print("\n segunda forma de usar metodo de brent")
        solu2=sc.brentq(f,intervalo[0],intervalo[1])
        print(formato.format(solu2))
        

for b in ndigitos:
    print("cantidad de digitos "+ str(b).split('-')[1])
    for i in range(-20,20):
        metodoBrent([i,i+1], b)
    print("")
