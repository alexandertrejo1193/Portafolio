#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May  8 11:17:53 2023

@author: alexandertrejo
"""

import random
import math
import matplotlib.pyplot as plt

def vapoiss(lambdaa= None,k= None):
    if k == None or lambdaa == None:
        lambdaa = float(input("Ingresar nÃºmero de ocurrencias en el intervalo de tiempo(lambda): "))
        k = int(input("Ingresar nÃºmero de iteraciones: "))
    while k<=0:
        k=int(input("Ingresar número de iteraciones mayor a 0: "))
    while lambdaa<0:
        lambdaa=float(input("Ingresar número de ocurrencias positivs: "))
    lista=[]

    for i in range(1,k+1):
      p=math.exp(-lambdaa)
      u = random.random()
      i = 0
      corredora=0
      F=p
      while corredora==0:
        if u < F:
          corredora=1
        else:
          p*=lambdaa/(i+1)  
          F += p
          i = i + 1
      lista.append(i)
       
    return(lista)