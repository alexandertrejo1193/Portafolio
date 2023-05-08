#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May  8 11:17:53 2023

@author: alexandertrejo
"""

import random
import math
import matplotlib.pyplot as plt

def acepyrecha(k=int(input("Ingresar número de iteraciones: "))):
    while k<=0:
        k=int(input("Ingresar número de iteraciones mayor a 0: "))
    lista3=[]
    for i in range(0,k):
      x=[1,2,3,4,5,6,7,8,9,10]
      probabilidades=[.11,.12,.09,.08,.12,.10,.09,.09,.10,.10]
      n=10
      qj=[1/10,1/10,1/10,1/10,1/10,
          1/10,1/10,1/10,1/10,1/10]
      lista2=[]
      for i in range(0,len(x)):
        cociente=probabilidades[i]/qj[i]
        lista2.append(cociente)
      c=max(lista2)
      u1=random.random()
      y=math.trunc(n*u1)+1
      u2 = random.random()
      if u2<=probabilidades[y-1]/(c*qj[y-1]):
        X=y
      while u2>probabilidades[y-1]/(c*qj[y-1]):
        u1=random.random()
        y=math.trunc(n*u1)+1
        u2 = random.random()
      X=y
      lista3.append(X)
    promedio=sum(lista3)/len(lista3)
    print(f"la simulación de la variable aleatoria es {promedio}")
    lista1=[]
    for i in range(0,len(x)):
      almacenadora=x[i]*probabilidades[i]
      lista1.append(almacenadora)
    esperanza=sum(lista1)
    plt.hist(lista3)
    print(f"El error es {abs(promedio-esperanza)}")
acepyrecha()