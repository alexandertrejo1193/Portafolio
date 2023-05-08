#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May  8 11:17:53 2023

@author: alexandertrejo
"""

import random
import math
import matplotlib.pyplot as plt

def vabinomial(k= None,n=None,p=None):
    if k == None or n == None or p==None:
        n = float(input("Ingresar nÃºmero de ocurrencias en el intervalo de tiempo(lambda): "))
        k = int(input("Ingresar nÃºmero de iteraciones: "))
        p =float(input("ingresar probabilidad de éxito "))
    while n<=0:
        n=int(input("Ingresar n mayor a 0: "))
    while k<=0:
        k=int(input("Ingresar número de iteraciones mayor a 0: "))
    while p <0 or p>1:
      print("Ingrese una probabilidad entre 1 y 0")
      p=float(input("ingresar probabilidad de éxito "))
    lista=[]
    for j in range(1,k+1):
      u = random.random()
      i=0
      c=p/(1-p)
      pr=(1-p)**n
      F=pr
      corredora=0
      while corredora==0:
        if u < F:
          corredora=1
        else:
          pr*=c*(n-i)/(i+1)
          F+=pr
          i+=1
      lista.append(i)
    return(lista)

def bernoulli (k=None,p=None):
    return(vabinomial(k,1,p))