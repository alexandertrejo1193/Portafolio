#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May  8 11:17:53 2023

@author: alexandertrejo
"""

import random
import math
import matplotlib.pyplot as plt

def vaexp(k=None,lamb=None):
    if k == None  or lamb==None:
        k=int(input("Ingresa el numero de simulaciones: "))
        lamb=float(input("Ingresa el valor de lambda: "))
    while k<=0:
           k=int(input("Ingresar número de iteraciones mayor a 0: "))
    while lamb<0:
        lamb=float(input("Ingresar número de ocurrencias positivs: "))
    resultados=[]
    for j in range (0,k):
        u = random.random()
        x = (-1 / lamb) * math.log(u)
        resultados.append(x)
    return(resultados)