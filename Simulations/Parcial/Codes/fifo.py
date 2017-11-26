#!/usr/bin/python
import subprocess
import numpy as np

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




def ClientesOut(aif,sif,dif,tif,a):

    i=0
    cont=0
    contout=0
    while(i<a):
       if(tif[i]>=dif[i]):
          cont=cont+1
       else:
	  contout=contout+1
       i=i+1
    print "Clientes seguros", str(cont)
    print "Cliente que no soportaron", str(contout)


def organize(Arrival_t, Service_t, Tolerance_t):
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
    #Retornando datos
    return Arrival_t, Service_t, Tolerance_t

if __name__ == "__main__":

 di = []

# ai= np.random.normal(53.5,21.2442,50)
# si= np.random.uniform(0.0,6.0,50)
 ai = [8,14,16,19,30,31,32,33,33,34,35,37,37,44,46,46,46,47,47,48,49,50,51,51,51,52,52,54,54,54,56,57,58,60,63,64,66,67,69,71,71,76,76,77,80,87,87, 87, 93,110]
 si = [5, 4, 4, 5, 2, 1, 4,1, 1, 3, 4, 6, 3, 1, 2, 5, 5, 6, 2, 3, 3, 5, 1, 3, 3, 5, 6, 1, 3, 1, 2, 2, 2, 4, 6, 5, 5, 1, 1, 5, 4, 4, 2, 5, 3, 3, 5, 3, 3, 4]
 bi = []
 ti = np.random.normal(10,2,50)

 ai,si,ti = organize(ai,si,ti)

 for g in range(50):
   ai[g]=round(ai[g])
   si[g]=round(si[g])
   ti[g]=round(ti[g])




 di = delay(ai,si,50)
 Ssi=0.0
 for x in range(0, len(si)):
   Ssi=Ssi+si[x]
 Stsi=Ssi/50
 Sai=0.0
 for x in range (50):
   Sai=Sai+ai[x]
 Stai=Sai/50
 subprocess.call(['clear', ''])

 for x in range(50):
   bi.insert(x , ai[x]+di[x])

 print "********************************************"
 print "Arrival time /  Service begin  / Delay time  / Service time / Tolerance"
 for x in range(50):
  print "a"+ str(x+1) +":"  + str(ai[x]) + "       ->    b" + str(x+1) +":"  + str(bi[x]) + "   ->   d"+ str(x+1) +":"  + str(di[x]) + "   ->   s"+ str(x+1) +":"  + str(si[x]) + "    ->  t" + str(x+1)+":" + str(ti[x])

 print ("********************************************")

 print "Statistics of service time = " + str(Stsi)
 print "Statistics of arrival time = " + str(Stai)

 ClientesOut(ai,si,di,ti,50)
