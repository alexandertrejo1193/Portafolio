#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May  8 11:17:53 2023

@author: alexandertrejo
"""

import random
import math
import matplotlib.pyplot as plt
import numpy as np
##______________#FUNCION DE PROCESO POISSON NO HOMOGENO#_______________#
def ppoiss(lambdaa=None, k=None, t=None):
    #ℷ(t)=t+10
    if k == None or t == None or lambdaa == None:
        lambdaa = float(input("Ingresar nÃºmero de ocurrencias en el intervalo de tiempo(lambda): "))
        k = int(input("Ingresar nÃºmero de iteraciones: "))
        t = float(input("Ingresar el tiempo: "))
    while k <= 0:
        k = int(input("Ingresar nÃºmero de iteraciones mayor a 0: "))
    while t <= 0:
        t = float(input("Ingresar el tiempo mayor a 0: "))
    while lambdaa < 10+t:
        lambdaa = float(input("Ingresar nÃºmero de ocurrencias mayor a 110: "))
    listaa22 = []
    listas=[]
    for i in range(0, k):
        tiempo = 0
        bandera = 0
        contador = 0
        lista33=[]
        while bandera == 0:
            tiempo += -(1 / lambdaa) * math.log(random.random())
            if tiempo > t:
                bandera = 1
            else:
                u=random.random()
                if u <= (tiempo+10)/lambdaa:
                    contador += 1
                    lista33.append(tiempo)
            n = contador
        listaa22.append(n)
        listas.append(lista33)
    
    resultados={"contadores":listaa22,"listas":listas}
    return (resultados)
#______________________________________________________________________________#
##___________________________#SISTEMA DE COLAS#_______________________________#
def entradasysalidas(lambdaa=None, k=None, t=None):
    simulacion=ppoiss(lambdaa, k, t) #utilizamos la funcion de arriba para traer 2 simulaciones que seran las entradas y salidas
    entradas=simulacion["listas"][0]
    salidas=simulacion["listas"][1]
    salidas1=[] #utilizamos esta lista para poder eliminar todos los tiempos anteriores a la primera entrada
    #entradas=[.3,.4,.6]  #ejemplo de clase, si se quiere utilizar solo quitar gato en las entradas y salidas
    #salidas=[.1,.33,.8,.9]
    
    #ciclo para quitar todos los tiempos anteriores a la primera entrada
    for i in range(0,len(salidas)):
        try: #lo que hace es intentar el ciclo, si no se puede en vez de mandar error hace lo que diga el except, en este caso queremos que ya no continue
            if entradas[0]<salidas[i]:
                salidas1.append(salidas[i])
        except:
            break
    
    salidas=salidas1 #tenemos una lista nueva sin los tiempos que son menores a la primera entrada
    #creamos listas para almacenar y variables que nos serviran para la simulacion
    N=0
    i=1
    listadeNs=[0]
    lineadetiempo=[0]
    
    #este algoritmo lo que hace, es hacer una linea del tiempo
    #despues busca las posiciones de cada entrada y salida con respecto a la linea del tiempo
    #se comparan las posiciones con las lineas del tiempo y condicionamos para que nos regrese N que es nuestro contador
    #hacemos la linea del tiempo
    lineadetiempo.extend(entradas)
    lineadetiempo.extend(salidas)
    lineadetiempo.sort()
    #vamos a sacar las posiciones de las entradas y salidas respecto a la linea del tiempo
    n1=[]
    n2=[]
    for i in range(0,len(entradas)):
        for j in range(0,len(lineadetiempo)):
            if entradas[i]==lineadetiempo[j]:
                n1.append(j)
         
    for i in range(0,len(salidas)):
        for j in range(0,len(lineadetiempo)):
            if salidas[i]==lineadetiempo[j]:
                n2.append(j)
    #condicionamos para que N (o contador) sea 1 cuando entre y -1 cuando salga
    for i in range(0,len(lineadetiempo)):
        for j in range(0,len(n1)):
            if lineadetiempo[i]==lineadetiempo[n1[j]]:
                N+=1
                if N<0:
                    N=0
                listadeNs.append(N)
            try: 
                if lineadetiempo[i]==lineadetiempo[n2[j]]:
                    
                    N-=1
                    if N<0:
                        N=0
                    listadeNs.append(N)
            except:
                break
    #guardamos resultados
    resultado={"Linea de Tiempo":lineadetiempo,"Sistema":listadeNs,
               "Tiempos de entradas":entradas,"Tiempos de salidas":salidas,
               "Posicion entradas":n1,"Posicion salidas":n2}
    return(resultado)
##______________#GRAFICA#_______________#
#Hacemos un ejemplo para la grafica, lo asignamos a una variable apra que no cambien los resultados
sistemadecolas=entradasysalidas(110,2,.5)
#Hacemos un ciclo para hacer la grafica 
for i in range(0,len(sistemadecolas["Sistema"])):
    plt.hlines(sistemadecolas["Sistema"][i], xmin=i, xmax=i+1)
    plt.plot(i,sistemadecolas["Sistema"][i],'-ro')
plt.title("Sistema de colas gráfico escalonado")
plt.xlabel("Tiempo")
plt.ylabel("N personas en el tiempo t")
if len(sistemadecolas["Sistema"])<20 :
    indice = np.arange(len(sistemadecolas["Sistema"]))   
    plt.xticks(indice)
indice2 = np.arange(max(sistemadecolas["Sistema"])+1)   
plt.yticks(indice2)#el eje y nos salia con .5 entonces cambiamos el eje para que saliera puro entero
#*nota: no cambiamos el eje x por los tiempos reales porque se saturaba a la vista
print(f"El sistema de colas es el siguiente:\n {sistemadecolas['Sistema']} \nCon los tiempos de entrada: \n{sistemadecolas['Tiempos de entradas']}\nCon los tiempos de salida: \n {sistemadecolas['Tiempos de salidas']}")

    