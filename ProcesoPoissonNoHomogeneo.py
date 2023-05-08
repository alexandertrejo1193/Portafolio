import random
import math
import matplotlib.pyplot as plt


def ppoiss(lambdaa=None, k=None, t=None):
    #ℷ(t)=t+10
    if k == None or t == None or lambdaa == None:
        lambdaa = float(input("Ingresar nÃºmero de ocurrencias en el intervalo de tiempo(lambda): "))
        k = int(input("Ingresar nÃºmero de iteraciones: "))
        t = int(input("Ingresar el tiempo: "))
    while k <= 0:
        k = int(input("Ingresar nÃºmero de iteraciones mayor a 0: "))
    while t <= 0:
        t = int(input("Ingresar el tiempo mayor a 0: "))
    while lambdaa < 10+t:
        lambdaa = float(input("Ingresar nÃºmero de ocurrencias mayor a 110: "))
    listaa22 = [0]
    listas=[0]
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

#------------------------------------------------------------------------------
#Ejemplo graficando una lista

listaaa=[]
procp=ppoiss(110,5, 3) #para que no haya un cambio en los numeros aleatorios lo
# asignamos a una variable
#Generamos el eje x
for i in range(0,procp["contadores"][1]):
    listaaa.append(i)
#imprimimos contadores y listas
print(f"El numero de personas en la lista es: {procp['contadores']}")
print(f"Los tiempos simulados son: {procp['listas']}")
#Grafico con una lista 
plt.plot(listaaa,procp["listas"][1],marker='o', color = 'm', label = "Lista 1")
plt.title("Proceso Poisson No Homogeneo")
plt.xlabel("Personas")
plt.ylabel("Tiempo")
plt.legend(loc = "upper left")

#------------------------------------------------------------------------------
#Ejemplo graficando todas las listas

procp=ppoiss(110,5, 3) #para que no haya un cambio en los numeros aleatorios lo
# asignamos a una variable
#Generamos el eje x
for i in range(0,len(procp["contadores"])):
    listaaa=[]
    for j in range(0,procp["contadores"][i]):
        listaaa.append(j) 
    plt.plot(procp["listas"][i],marker='o', label = f"Lista {i+1}")
#imprimimos contadores y listas
print(f"El numero de personas en cada lista son: {procp['contadores']}")
print(f"Los tiempos simulados son:  {procp['listas']}")

#Grafico con todas las listas
plt.title("Proceso Poisson No Homogeneo")
plt.xlabel("Personas")
plt.ylabel("Tiempo")
plt.legend(loc = "upper left")

#------------------------------------------------------------------------------
#Hobbie (grafico escalonado)


listaaa=[]
listaaa2=[]
procp=ppoiss(110,5, 3) #para que no haya un cambio en los numeros aleatorios lo
# asignamos a una variable
#Generamos el eje x
for i in range(0,len(procp["contadores"])-1):
    listaaa.append(i)

procp["contadores"].pop(0) #le quitamos el 0 que le agregamos para la 
#otra gráfica
for i in listaaa:
    plt.hlines(y=procp["contadores"][i], xmin=i, xmax=i+1)
    plt.plot(i,procp["contadores"][i],'-ro')
plt.title("Proceso Poisson No Homogeneo escalonado")
plt.xlabel("Tiempo")
plt.ylabel("Personas en el tiempo t")
