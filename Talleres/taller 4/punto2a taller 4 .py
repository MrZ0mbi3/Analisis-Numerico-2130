# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import math
import numpy as np
from matplotlib import pyplot as plt

tx=[]
ty=[]

def funcion(t,y):
    return (t**(3*t))-40*y

def metodoEuler(a,b,y0,n):
    
    h=(b-a)/n
    t0=a
    i=0
    while i< n:
        ty.append(i)
        y1=y0+(h*funcion(t0,y0))
        t0=a+i*h
        y0=y1
        print("(",t0,",",y0,")")
        tx.append(t0)
        i=i+0.1
    

metodoEuler(1, 2, 10, 10)
plt.plot(tx,ty)
plt.show()