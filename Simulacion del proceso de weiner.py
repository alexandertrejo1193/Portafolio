#simulacion del proceso de Weiner
import random
import matplotlib.pyplot as plt

def ProcesodeWeiner(H,N,a):  
   dt=1/N
   S=[0]
   St=0
   x=[0]
   while H<=0:
       H=int(input("Ingresar horizonte mayor a 0: "))
   while N<=0:
       N=int(input("Ingresar N mayor a 0: "))
   for i in range(0,N*H):
       E=random.uniform(-a,a)
       St=St+((dt)**(1/2)*E)
       S.append(St)
       x.append((1+i)/N)
   resultados={"eje_x":x,"S":S}
   return resultados
procesodeweiner=ProcesodeWeiner(5,10,1)   

print(f'La lista de Ss es: {procesodeweiner["S"]}')
plt.plot(procesodeweiner["eje_x"],procesodeweiner["S"])