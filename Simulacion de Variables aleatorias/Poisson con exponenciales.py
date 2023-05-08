#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May  8 11:17:53 2023

@author: alexandertrejo
"""

import random
import math
import matplotlib.pyplot as plt

def vapoissonconexp(lambdaa=float(input("Ingresar número de ocurrencias en el intervalo de tiempo(lambda): ")),k= int(input("Ingresar número de iteraciones: "))):
    while k<=0:
        k=int(input("Ingresar número de iteraciones mayor a 0: "))
    while lambdaa<0:
        lambdaa=float(input("Ingresar número de ocurrencias positivas: "))
    x=[]
    for i in range(1,k+1):
        contador=1
        u=random.random()
        while u>=math.exp(-lambdaa):
            u*=random.random()
            contador+=1
        valor= contador-1
        x.append(valor)
    print(f"La simulación de la variable aleatoria es {sum(x)/len(x)}")
    print(f"El error es de {abs(sum(x)/len(x)-lambdaa)}")
    #plt.hist(x)
vapoissonconexp()