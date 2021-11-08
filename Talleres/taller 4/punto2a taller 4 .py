# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import math
import numpy as np
from matplotlib import pyplot as plt
from matplotlib import style
style.use('ggplot')

tx=[]
ty=[]
tyExacta=[]
error=[]

def funcionExacta(t):
    return ((1/43)*t*math.e**(3*t))-((math.e**(3*t))/1849)

def funcion(t,y):
    return (t*math.e**(3*t))-40*y

def metodoEuler(a,b,y0,n):
    tx.append(a)
    ty.append(y0)
    t0=a
    tyExacta.append(funcionExacta(t0))
    print("exacta ","(",t0,",",funcionExacta(t0),")")
    print("euler ","(",t0,",",y0,")")
    h=(b-a)/n
    
    
    for i in range(n):
        tyExacta.append(funcionExacta(t0))
        print("exacta ","(",t0,",",funcionExacta(t0),")")
        y0=y0 + h*funcion(t0,y0) 
        error.append(abs((funcionExacta(t0)-y0)/funcionExacta(t0)))
        ty.append(y0)
        t0=t0+h
        tx.append(t0)
        
        print("euler ","(",t0,",",y0,")")
    
    

metodoEuler(0, 2, 10, 100)
plt.plot(tx,ty)
plt.show()

plt.plot(tx, tyExacta)
plt.show()

suma=0
print(error)

for i in range(3,len(error)):
    
    suma=suma+error[i]

errorPromedio=suma/len(error)
print(errorPromedio)