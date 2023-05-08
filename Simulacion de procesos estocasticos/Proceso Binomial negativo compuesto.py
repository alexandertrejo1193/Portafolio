#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May  8 11:17:53 2023

@author: alexandertrejo
"""

import random
import math
import matplotlib.pyplot as plt

from funciones import vabinomial,vaexp,vagamma,vapoiss,vabinneg
import matplotlib.pyplot as plt
 
def colectivopoiss(k=None,n=None,lamb1=None,lamb2=None):
    ExpoGamma = input("Escriba si, si quiere que el procedimiento sea con exponencial, sino escriba no:")
    while lamb1>n:
        print("lambda debe ser menor a n")
        lamb1 = float(input("Ingresar lambda: "))
        k = int(input("Ingresar numero de iteraciones: "))
    lista1=[]
    for i in range(0,k):
        N=vapoiss(lamb1,1)[0]
        while N==0:
            N=vapoiss(lamb1,1)[0]
        if ExpoGamma=="si" or ExpoGamma=="Si" or ExpoGamma=="SI" or ExpoGamma=="sI" :
            lista=vaexp(N,lamb2)
        else:
            lista=vagamma(N,lamb2,N)
        S=sum(lista)
        lista1.append(S)
    return(lista1)
prueba=colectivopoiss(1000,30,10,8)
print(f"La lista de k montos es :{len(prueba)}")
plt.hist(prueba)





