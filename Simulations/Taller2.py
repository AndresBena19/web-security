#!/usr/bin/python

import subprocess


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





if __name__ == "__main__":

 di = []
 ai = [0,1,1,1,1,2,2,3,3,3,4,5,5,6,6,7,8,8,8,8]
 si = [4,3,3,3,5,3,5,3,4,5,2,3,4,1,4,4,1,2,4,5]

 di = delay(ai,si,20)
 
 x=1;
 Ssi=0.0;
 for x in range(20):
   Ssi=Ssi+si[x]
 Stsi=Ssi/20

 Sai=0.0;
 for x in range (1, 20):
   Sai=Sai+ai[x] 
 Stai=Sai/20

 subprocess.call(['clear', ''])

 

 print "********************************************"
 print "Arrival time /  Service time  / Delay time  / Service begin"
 for x in range(20):
  print "a"+ str(x+1) +":"  + str(ai[x]) + "       ->    s" + str(x+1) +":"  + str(si[x]) + "   ->   di"+ str(x+1) +":"  + str(di[x])

 print "********************************************"

 print "Statistics of service time = " + str(Stsi) + " customer per unit time"
 print "Statistics of arrival time = " + str(Stai) + " customer per unit time"

