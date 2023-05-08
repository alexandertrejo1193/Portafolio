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
 
def colectivobinneg(k=None,p=None,n=None,lamb=None):
    ExpoGamma = input("Escriba si, si quiere que el procedimiento sea con exponencial, sino escriba no:")
    lista1=[]
    for i in range(0,k):
        N=vabinneg(1,p,n)["lista"][0]
        if ExpoGamma=="si" or ExpoGamma=="Si" or ExpoGamma=="SI" or ExpoGamma=="sI" :
            lista=vaexp(N,lamb)
        else:
            lista=vagamma(N,lamb,N)
        S=sum(lista)
        lista1.append(S)
    return(lista1)

prueba=colectivobinneg(1000,.8,20,5)
print(f"La lista de k montos es :{len(prueba)}")
plt.hist(prueba)




