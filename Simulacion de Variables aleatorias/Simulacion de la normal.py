#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May  8 11:17:53 2023

@author: alexandertrejo
"""

import random as rd
import math
import statistics as sta

def absnormal():
    bandera = 0
    contador = 0
    while bandera == 0:
        y1 = -math.log(rd.random())  
        y2 = -math.log(rd.random())

        valor = math.exp(-((y1 - 1) ** 2) / 2)  
        if y2 > valor:
            contador = contador + 1
            bandera = 0
        else:
            bandera = 1
            contador = contador + 1
            x = y1
    return {"x": x ,"contador": contador}

def sdnorm():
    x = []
    contador = []
    u1 = rd.random()
    y = absnormal()
    if .5 > u1:
      x.append(y["x"])
      contador.append(y["contador"])
    else:
      x.append(-y["x"])
      contador.append(y["contador"])
    return {"lista": x ,"contador": contador}
        


def rnorm(sim,media,desvest):
    while sim<=0:
        sim=int(input("Ingresar n�mero de simulaciones mayor a 0: "))
    while desvest<=0:
        desvest=int(input("Ingresar desviaci�n estandar mayor a 0: "))
    lista = []
    for i in range(0,sim):
        X = media + desvest * sdnorm()["lista"][0]
        lista.append(X)
    return lista
#Ejemplo de la función
print(f'La lista de las simulaciones es : {rnorm(10,2,1)}')
print(f'La media de las simulaciones es : {sta.mean(rnorm(10,2,1))}')