#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May  8 11:17:53 2023

@author: alexandertrejo
"""

import random
import math
import matplotlib.pyplot as plt

def vageometrica(k=None,p=None):
    if k == None  or p==None:
        k = int(input("Ingresar nÃºmero de iteraciones: "))
        p =float(input("ingresar probabilidad de éxito "))

    while k<=0:
        k=int(input("Ingresar número de iteraciones mayor a 0: "))
    while p <0 or p>1:
      p=float(input("Inserte una probabilidad entre 0 y 1: "))
    listaa1=[]
    for i in range(0,k):
        u=random.random()
        x=math.trunc(math.log10(u)/math.log10(1-p))+1
        listaa1.append(x)
    return(listaa1)