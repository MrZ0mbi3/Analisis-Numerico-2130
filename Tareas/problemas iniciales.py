# -*- coding: utf-8 -*-
"""
Created on Thu Jul 22 10:14:43 2021

@author: samyf
"""
"""
primer punto
"""
#%%
import numpy as np
from time import time
from matplotlib import pyplot as plt
tolerancia = [10**-8, 10**-16,10**-32,10**-64] 

def raizCuadrada(n, errorP, x ):
    formato="{:."+str(errorP).split('-')[1]+"f}"
    tInicial=time()
    tiempos=[0]
    errorAbsoluto=[x]
    errorRelativo=[0]
    print("Raiz cuadrada de ",n, " Con error de ", errorP  )
    y=np.longdouble((x+(n/x))*0.5)
    while abs(x-y) > errorP:
        errorAbsoluto.append(abs(x-y))
        errorRelativo.append(abs((x-y)/x))
        tiempos.append(time()-tInicial)
        x=y
        y=np.longdouble((x+ (n/x))* 0.5)
        print(formato.format(y))
    print("Resultado: ",formato.format(y))
    plt.plot(tiempos,errorAbsoluto)
    plt.show()
    plt.plot(tiempos,errorRelativo)
    plt.show()
    
    eficacia(errorAbsoluto)
#round(y, int(str(errorP).split('-')[1]) )    

#%% 
def eficacia(errores):
    error=[]
    errorsig=[]
    for i in range(len(errores)-1):
        error.append(errores[i])
        errorsig.append(errores[i+1])
    
    print("Relacion entre errores")
    plt.plot(error,errorsig)
    plt.show()
        
    

#%%
for i in tolerancia:
    raizCuadrada(7,i,1000)

#%%
"""
Punto 4 
"""
import numpy as np
import random
from time import time
def llenadoMatriz(matriz,porcentaje):
    print(int(len(matriz)*(porcentaje/100)))
    for i in range(int(len(matriz)*(porcentaje/100))):
        x=random.randint(i,len(matriz)-1)
        y=random.randint(0,len(matriz[0])-1)
        matriz[x][y]=0
        
def puntajeDeCadaDia(matriz):
    
    for i in range(int(len(matriz[0]))):
        suma=0
        for j in range(int(len(matriz))):
            suma=suma+matriz[j][i]
        print("Puntaje total dia ", i +1, ": ",suma)

tiempoInicial=time()
matriz = []
filas=450
columnas=450
medidas=[0.5 ,1]

for i in range(filas):
    
    matriz.append([random.choice(medidas)]*columnas)
    for j in range(columnas):
        matriz[i][j]=random.choice(medidas)
    
    

print(matriz)

llenadoMatriz(matriz,60)
print(matriz)

puntajeDeCadaDia(matriz)
print("Matriz normal \n",np.matrix(matriz))


#https://numpy.org/doc/stable/reference/generated/numpy.linalg.pinv.html#numpy.linalg.pinv
inversa=np.linalg.inv(matriz)
#inversa=np.matrix(matriz)
print ("Matriz inversa \n",inversa)

tiempoEjecucion=time()-tiempoInicial
print("tiempo de ejecucion:",tiempoEjecucion)


#%%
import math
print(math.pi)
print(math.inf)
float('inf')








