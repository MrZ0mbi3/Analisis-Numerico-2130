# -*- coding: utf-8 -*-
import sympy 
import numpy 
import math


sympy.init_printing(use_latex="mathjax", use_unicode=False, wrap_line=False)
x = sympy.Symbol('x')
print("usando libreria")

print(float(sympy.integrate(1/(1+x**2)**3, (x, 1, math.inf))))

print(float(sympy.integrate(sympy.sin(x)/x, (x, 0, 1))))
