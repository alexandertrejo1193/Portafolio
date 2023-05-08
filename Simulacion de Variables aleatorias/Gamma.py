#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May  8 11:17:53 2023

@author: alexandertrejo
"""

import random
import math
import matplotlib.pyplot as plt

def vagamma(k=None,lamb=None,n=None):
    if k == None  or lamb==None or n==None:
        k=int(input("Ingresa el numero de simulaciones: "))
        lamb=float(input("Ingresa el valor de lambda: "))
        n=int(input("Ingresa el numero de exponenciales: "))
    while k<=0:
        k=int(input("Ingresar número de iteraciones mayor a 0: "))
    while n<=0:
        n=int(input("Ingresar número de exponenciales mayor a 0: "))
    while lamb<0:
        lamb=float(input("Ingresar número de ocurrencias positivas: "))
    x=[]
    for j in range(1,k+1):
        valor=0
        for i in range(1,n+1):
            valor=valor -((1/lamb)* math.log(random.random()))
        x.append(valor)
    return(x)