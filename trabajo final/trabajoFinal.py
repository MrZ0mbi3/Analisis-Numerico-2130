# -*- coding: utf-8 -*-
"""
Created on Fri Nov 19 16:52:11 2021

@author: juank
"""

import numpy as np
import csv
import matplotlib.pyplot as plt
from scipy.integrate import odeint
from scipy.integrate import solve_ivp

# ----------Susceptible - Infectado - Recuperado-----------
def modelo_SIR(y, tasaInfec, tasaRecup, tiempoMax):
  # s: Población susceptible
  # i: Población infectada
  # r: Población recuperada
  # n: (implícito) conjunto de s, i, r (s+i+r)
  dS_dt = -tasaInfec * s * i / (s + i + r)
  dI_dt = tasaInfec * s * i / (s + i + r) - (tasaRecup * i)
  dR_dt = tasaRecup * i
  return([dS_dt, dI_dt, dR_dt])

# Datos iniciales:
# N: Población de
N = 45000
I0 = 10/N
# S0: N (población de Santa Marta) - I0 (primer infectado)
S0 = N - I0
# R0: Número inicial de Recuperados (NO CONFUNDIR CON NÚMERO DE REPRODUCCIÓN)
R0  = 1.5
#= 0ec
tasaRecup = 0.022

B = 0.06
C = 1.5
Y = 0.021

# t: 60 días (2 meses)
# Tercer parámetro total de muestras en el rango 0 - 60 (parámetro 2)
tSIR = np.linspace(0, 60, 60)

# Solución con MÉTODO: Runge-Kutta de Orden 4
# Basado en:
# http://acme.byu.edu/wp-content/uploads/2020/09/SIR2020.pdf


def ode_SIR(t, y):
  return np.array([-tasaInfec*y[0]*y[1]/N, (tasaInfec*y[0]*y[1]/N)-tasaRecup*y[1], tasaRecup*y[1]])

# -----------------Punto 1-------------------------------
sol_SIR2 = solve_ivp(ode_SIR, [tSIR[0], tSIR[-1]], [S0, I0, R0], method = "RK45", t_eval = tSIR,dense_output=True)

#print(sol_SIR2)
# Gráfica

plt.figure(figsize = [6, 4])
plt.plot(sol_SIR2.t, sol_SIR2.y[0], label = "S(t)")
plt.plot(sol_SIR2.t, sol_SIR2.y[1], label = "I(t)")
plt.plot(sol_SIR2.t, sol_SIR2.y[2], label = "R(t)")
plt.grid()
plt.legend()
plt.title("SIR marzo 20 - mayo 20")
plt.xlabel("Tiempo")
plt.ylabel("No. Individuos")
plt.show()

print("Tabla de solución del mes de marzo 20 – mayo 20")

print('Dia','Susceptibles','Infectados','Recuperados')
for i in range(len(tSIR)):
  print(i+1,sol_SIR2.y[0][i], sol_SIR2.y[1][i], sol_SIR2.y[2][i])

t1SIR = np.linspace(0, 365, 365)

# -----------------Punto 2-------------------------------
print("Pronostico de la pandemia en un año")
sol_SIR3 = solve_ivp(ode_SIR, [t1SIR[0], t1SIR[-1]], [S0, I0, R0], method = "RK45", t_eval = t1SIR)

#plt.figure(figsize = [6, 4])
plt.axis([0, 360, 0, 50000])
plt.plot(sol_SIR3.t, sol_SIR3.y[0], label = "S(t)")
plt.plot(sol_SIR3.t, sol_SIR3.y[1], label = "I(t)")
plt.plot(sol_SIR3.t, sol_SIR3.y[2], label = "R(t)")
plt.grid()
plt.legend()
plt.title("Pronostico de la pandemia en un año")
plt.xlabel("Tiempo")
plt.ylabel("No. Individuos")
plt.show()

# Tasas de modelo pronóstico:
# Manrique-Abril, et al.
# tasaInfec ≠ porcentaje
#tasaInf

#------------------Punto 3----------------------------

diaMayorContagios=0
cantidadContagios = 0
for i in range(len(sol_SIR3.y[1])):
  if(sol_SIR3.y[1][i] > cantidadContagios ):
    diaMayorContagios = i
    cantidadContagios =  sol_SIR3.y[1][i]

print("Punto 3: Dia con mayor contagios:")
print(diaMayorContagios)
print("Cantidad de contagios el dia",diaMayorContagios,":")
print(cantidadContagios)
      
  




