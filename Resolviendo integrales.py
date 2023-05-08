

import random
import math
#ejercicio número 1
k=int(input("Número de iteraciones(positivo y entero): "))
while k<=0:
  print("Ingrese un número positivo ")
  k=int(input("número de iteraciones"))
suma=0
for i in range(1,k+1):
  u=random.uniform(0,1)
  suma+=math.exp(u**2)
print(f"La aproximación de la integral es {suma/k} ")

import random
import math
#ejercicio número 2
k=int(input("Número de iteraciones(positivo y entero): "))
a=int(input("Valor de a: "))
b=int(input("Valor de b: "))

while k<=0:
  print("Ingrese un número positivo ")
  k=int(input("número de iteraciones"))

suma=0
for i in range(1,k+1):
  u=random.uniform(0,1)
  suma+=(b-a)*math.exp((a+(b-a)*u)**2)

promedio=(suma/k)
print(f"La aproximación de la integral es {promedio} ")

import random
import math
#ejercicio número 3
k=int(input("Número de iteraciones(positivo y entero): "))

while k<=0:
  print("Ingrese un número positivo ")
  k=int(input("Número de iteraciones"))


suma=0
for i in range(1,k+1):
  u=random.uniform(0,1)
  suma+=math.exp(-(1/u-1))/u**2

print(f"La aproximación de la integral es {suma/k} ")

import random
import math
#ejercicio número 4
k=int(input("Número de valores(positivo y entero): "))
while k<=0:
  print("Ingrese un número positivo  ")
  k=int(input("Número de valores(positivo y entero): "))


lista=[]
for j in range(1,k+1):
  s=0
  n=0
  while s<=1:
    s+=random.uniform(0,1)
    n+=1
  lista.append(n)
suma=0
for i in lista:
  suma+=i


promedio=suma/k

#metodo #2 quitar el ciclo y en promedio= sum(lista)/len(lista)
print(f"La lista de los contadores es {lista}")
print(f"El valor promedio es de {promedio}")