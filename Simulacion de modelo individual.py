#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May  8 11:17:53 2023

@author: alexandertrejo
"""

import random
import math
import matplotlib.pyplot as plt

from funciones import vapoiss, disbeta, bernoulli, vageometrica
def riesgoindividual(m=None,lambdaa=None):
    if m == None or lambdaa == None:
        lambdaa = float(input("Ingresar nÃºmero de ocurrencias en el intervalo de tiempo(lambda): "))
        m = int(input("Ingresar nÃºmero de iteraciones: "))
    #polizas
    numero_polizas=vapoiss(lambdaa,m)
    listadeSs=[]
    for Nn in numero_polizas:
        if Nn==0:
            S=0
        else:
            n=Nn
            #probabilidades q1,q2,...,qn
            probabilidades=disbeta(n)["simulaciones"]
            probabilidades2=disbeta(n)["simulaciones"]
            #Muertes D1,D2,...,Dn 
            D=[]
            #Reclamaciones C1,C2,...,Cn 
            C=[]
            for i in range(0,n):
                D.extend(bernoulli(1,probabilidades[i]))
                C.extend(vageometrica(k=1,p=probabilidades2[i]))
            #D_j C_j
            DC=[]
            for j in range(0,n):
                if D[j]==1:
                    DC.append(C[j])
                else:
                    DC.append(0)
            #Monto de reclamacion o agregado de reclamaciones S
            S=sum(DC)
        listadeSs.append(S)
    return(listadeSs)
print(f"La lista de los montos de reclamaciones es la siguiente: {riesgoindividual(10,2)}")




