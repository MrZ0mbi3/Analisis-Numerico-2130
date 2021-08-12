# -*- coding: utf-8 -*-
"""
Created on Wed Aug 11 21:26:53 2021

@author: samyf
"""
import numpy as np
import math

def f(x):
    #return np.longdouble(math.cos(x)*math.cos(x) - x**2)
    #return math.e**x-x-1
    #return x**3 -2*x**2 + (4/3)*x-(8/27)
    #return x**3- 2*x-5


def metodoSteffesen(p0,tol):
    formato="{:."+str(tol).split('-')[1]+"f}"

    maxIt=100
    i=1
    while i<=maxIt:
        p1=np.longdouble(p0+f(p0))
        p2=np.longdouble(p1+f(p1))
        
        if (p2- 2*p1 +p0) !=0:
            p=np.longdouble(p0- (p1-p0)**2 / (p2- 2*p1 +p0))
        else:
            p=np.longdouble(p0- (p1-p0)**2 / ((p2- 2*p1 +p0)+tol))
        
        
        if abs(p-p0)<tol:
            print("iteraciones", i)
            return formato.format(p)
        i=i+1
        p0=p
    return "No se encontro raiz"
    

print(metodoSteffesen(0.6666,10**-53))
