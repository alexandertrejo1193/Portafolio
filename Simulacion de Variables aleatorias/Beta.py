#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May  8 11:17:53 2023

@author: alexandertrejo
"""

import random
import math
import matplotlib.pyplot as plt

def disbeta(k=None):
  if k == None:
         k = int(input("Ingresar nÃºmero de iteraciones: "))
  while k<=0:
         k=int(input("Ingresar número de iteraciones mayor a 0: "))
  contador = [0]*k
  x = []
  a = 256 / 27
  for i in range (1,k+1):
    bandera = 0 
    while bandera ==0:
      U1 = random.random()
      U2 = random.random()
      valor = a * U1 * (1-U1) ** 3
      if U2 > valor:
        bandera = 0
        contador[i - 1] = contador[i-1] + 1
      else:
        bandera = 1
        contador[i-1] = contador[i-1] + 1
        x.append(U1)
  return {"simulaciones":x, "iteraciones": contador}