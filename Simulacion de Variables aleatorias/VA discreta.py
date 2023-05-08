#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May  8 11:17:53 2023

@author: alexandertrejo
"""

import random
import math
import matplotlib.pyplot as plt

def vadiscreta(n=int(input("Ingresar número de iteraciones: "))):
    listaaa1=[]
    for i in range(1,n+1):
        u=random.random()
        x=math.trunc(n*u)+1
        listaaa1.append(x)
    promedio=sum(listaaa1)/len(listaaa1)
    print(f"La simulación de la v.a. uniforme discreta es {promedio}")
    print(f"El error es de {abs((sum(listaaa1)/len(listaaa1))-((n+1)/2))} ")
    plt.hist(listaaa1)
vadiscreta()