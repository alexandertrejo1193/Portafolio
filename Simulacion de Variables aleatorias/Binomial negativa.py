#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May  8 11:17:53 2023

@author: alexandertrejo
"""

import random
import math
import matplotlib.pyplot as plt

def vabinneg(k=None,p=None,n=None):
    if k == None or p==None or n ==None:
        k = int(input("Ingresar nÃºmero de iteraciones: "))
        p =float(input("ingresar probabilidad de éxito "))
        n = int(input("ingresar el n-esimo exito "))
    while k<=0:
        k=int(input("Ingresar número de iteraciones mayor a 0: "))
    while p <0 or p>1:
        p=float(input("Inserte una probabilidad entre 0 y 1: "))
    while n<=0:
        n=int(input("Ingresar el n-esimo exito mayor a 0: "))
    lista=[]
    for i in range(0,k):
        simgeo=vageometrica(n,p)
        lista.append(sum(simgeo))
    resultados={"lista":lista,"promedio":sum(lista)/k}
    return resultados