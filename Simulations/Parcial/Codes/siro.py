#!/usr/bin/python
import subprocess
import numpy as np
import math



def delay(aif,sif,a):
 i=0
 di=[]
 ci=[]
 while (i<a):

      ai = aif[i]
      if (len(ci)!=0):
        if (ai < ci[i-1]):
           di.insert(i , ci[i-1]-ai)
        else:
           di.insert(i , 0)
      else:
        di.insert(i , 0)

      si = sif[i]
      ci.insert(i , ai+di[i]+si)
      i = i+1
 return di



def ClientesOut(aif,sif,dif,tif,prif,a):


    i=0

    cont=0
    time=0
    contout=0
    while(i<a):
       
        if((aif[i]+sif[i])<aif[i+1]):
            cont=cont+1
        else:
            if(prif[i+1]>prif[i]):
                dif[i]=dif[i]+sif[i+1]
                time=time+1
            if(time>=2):
                q=0
                while (q<=time):
                    dif[q]=dif[time]+si[time]
                    time=time-1
                    q=q+1
            
        i=i+1    


    while(b<a):
     if(tif[i]>=dif[i]):
         cont=cont+1
     else:
         contout=contout+1
     b=b+1
    print "Clientes seguros", str(cont)
    print "Cliente que no soportaron", str(contout)
    return  cont,contout


def prioridad(Priority,Arrival_t,Service_t, Tolerance_t):
    #ordenamos los datos de menor a mayor
    for i in range(0, len(Priority)):
        for j in range (0, len(Priority)):
            if (Priority[i]<Priority[j]):
                aux = Priority[i]
                Priority[i] = Priority[j]
                Priority[j] = aux
                #Change in the same way the service time
                aux = Service_t[i]
                Service_t[i] = Service_t[j]
                Service_t[j] = aux
                #Change in the same way the tolerance time
                aux = Tolerance_t[i]
                Tolerance_t[i] = Tolerance_t[j]
                Tolerance_t[j] = aux
                #Change in the same way the arrival time
                aux = Arrival_t[i]
                Arrival_t[i]=Arrival_t[j]
                Arrival_t[j]=aux

    #Retornando datos
    Arrival_t=Arrival_t[::-1]
    Service_t=Service_t[::-1]
    Tolerance_t=Tolerance_t[::-1]
    Priority=Priority[::-1]
    return Priority,Arrival_t,Service_t, Tolerance_t








def organize(Priority,Arrival_t, Service_t, Tolerance_t, Type):
    #ordenamos los datos de menor a mayor
    for i in range(0, len(Arrival_t)):
        for j in range (0, len(Arrival_t)):
            if (Arrival_t[i]<Arrival_t[j]):
                aux = Arrival_t[i]
                Arrival_t[i] = Arrival_t[j]
                Arrival_t[j] = aux
                #Change in the same way the service time
                aux = Service_t[i]
                Service_t[i] = Service_t[j]
                Service_t[j] = aux
                #Change in the same way the tolerance time
                aux = Tolerance_t[i]
                Tolerance_t[i] = Tolerance_t[j]
                Tolerance_t[j] = aux
                #Change in the same way the tolerance time
                aux = Priority[i]
                Priority[i] = Priority[j]
                Priority[j] = aux

    #Retornando datos
    if(Type):
       return Priority,Arrival_t, Service_t, Tolerance_t
    else:
       Arrival_t=Arrival_t[::-1]
       Service_t=Service_t[::-1]
       Tolerance_t=Tolerance_t[::-1]
       Priority=Priority[::-1]
       return Priority,Arrival_t, Service_t, Tolerance_t


def Siro(ai,si,bi,di,pri,a):
 di = delay(ai,si,10)
 Ssi=0.0
 
 for x in range(0, len(si)):
   Ssi=Ssi+si[x]

 Stsi=Ssi/10
 Sai=0.0

 for x in range (10):
   Sai=Sai+ai[x]

 Stai=Sai/10

 for x in range(10):
   bi.insert(x , ai[x]+di[x])


 print " Sistema de cola SIRO "
 print "********************************************"
 
 print "Arrival time /  Service begin     /    Delay time   /    Service time  /  Tolerance   /  Priority"
 for x in range(10):
  if(ti[x]<di[x]): 
     state="Desertor"
  else:
     state=""

  print "a"+ str(x+1) +":"  + str(ai[x]) + "       ->    b" + str(x+1) +":"  + str(bi[x]) + "   ->   d"+ str(x+1) +":"  + str(di[x]) + "   ->   s"+ str(x+1)  +":"  + str(si[x]) + "    ->  t" + str(x+1)+":" + str(ti[x]) + "    ->  p" + str(x+1)+":" + str(pri[x]) +  "  " + state 

 print ("********************************************")

 print "Statistics of service time = " + str(Stsi)
 print "Statistics of arrival time = " + str(Stai)

 cont, contout= ClientesOut(ai,si,di,ti,pri,10)
 return cont, contout


if __name__ == "__main__":

 di = []
 bi = []


 aiI=[49, 66, 87, 33, 60, 67, 64, 52, 47, 44, 87, 63, 68, 80, 8, 30, 14, 71, 33, 46, 110, 31, 34, 51, 19, 77, 51, 54, 93, 37, 76, 76, 87, 46, 52, 51, 71, 47, 57, 58, 48, 37, 35, 46, 16, 54, 50, 54, 56, 32]
 siI=[3, 5, 5, 1, 4, 1, 5, 5, 6, 1, 3, 6, 1, 3, 5, 2, 4, 4, 1, 5, 4, 1, 3, 3, 5, 5, 3, 1, 3, 3, 4, 2, 3, 5, 6, 1, 5, 2, 2, 2, 2, 6, 4, 2, 4, 3, 5, 3, 2, 4]
 PriI = [5, 1, 1, 3, 2, 0, 2, 0, 1, 4, 0, 3, 1, 4, 0, 3, 5, 3, 0, 0, 4, 0, 3, 1, 5, 2, 4, 2, 2, 3, 1, 0, 3, 5, 3, 3, 2, 5, 5, 4, 1, 0, 4, 2, 5, 4, 0, 2, 3, 4]

# aiI = [8,14,16,19,30,31,32,33,33,34,35,37,37,44,46,46,46,47,47,48,49,50,51,51,51,52,52,54,54,54,56,57,58,60,63,64,66,67,69,71,71,76,76,77,80,87,87, 87, 93,110]
# siI = [5, 4, 4, 5, 2, 1, 4,1, 1, 3, 4, 6, 3, 1, 2, 5, 5, 6, 2, 3, 3, 5, 1, 3, 3, 5, 6, 1, 3, 1, 2, 2, 2, 4, 6, 5, 5, 1, 1, 5, 4, 4, 2, 5, 3, 3, 5, 3, 3, 4]

 # Calculando media
 k = 0
 for i in aiI:
     k = k + i
 media = k/len(aiI)

 #Calculando desviacion estandar
 desviacion = np.std(aiI)


 acumFifo=0
 acumLifo=0
 acumSiro=0


 for c in range(1):

   #Generando valores aleatorios de tiempo de llegada
   ai= np.random.normal(media,desviacion,10)
   #Generando valores de tolerancia 
   ti = np.random.normal(10,2,10)
   #Generando valores aleatorios de tiempo de servicio
   Mx = max(siI)
   b = ((len(siI)+1)*Mx)/(len(siI)-1)
   si= np.random.uniform(0,b,10)
  #Generando valorea aletorios para la prioridad
   Mx1 = max(PriI)
   c = ((len(PriI)+1)*Mx1)/(len(PriI)-1)
   Pri=np.random.uniform(0,c,10)


   for g in range(10):
     ai[g]=round(ai[g])
     si[g]=round(si[g])
     ti[g]=round(ti[g])
     Pri[g]=round(Pri[g])



   bool=True
   pri,ai,si,ti = organize(Pri,ai,si,ti,bool)
   cont2,contout2 =  Siro(ai,si,bi,di,pri,10)


   #pri,ai,si,ti = prioridad(Pri,ai,si,ti)
   
   acumSiro=acumSiro+contout2


 print  "++++++++++++++++++++++++++++++++++++"
 print  "Promedio de desertores en SIRO:"+ str(acumSiro/100)
