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
 ai = [110, 93, 87, 87, 87, 80, 77, 76, 76, 71, 71, 69, 67, 66, 64, 63, 60, 58, 57, 56, 54, 54, 54, 52, 52, 51, 51, 51, 50, 49, 48, 47, 47, 46, 46, 46, 44, 37, 37, 35, 34, 33, 33, 32, 31, 30, 19, 16, 14, 8]
 si = [4, 3, 3, 5, 3, 3, 5, 2, 4, 4, 5, 1, 1, 5, 5, 6, 4, 2, 2, 2, 1, 3, 1, 6, 5, 3, 3, 1, 5, 3, 3, 2, 6, 5, 5, 2, 1, 3, 6, 4, 3, 1, 1, 4, 1, 2, 5, 4, 4, 5]
 bi = []

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
 print "Arrival time /  Service begin  / Delay time  / Service time"
 for x in range(50):
  print "a"+ str(x+1) +":"  + str(ai[x]) + "       ->    b" + str(x+1) +":"  + str(bi[x]) + "   ->   d"+ str(x+1) +":"  + str(di[x]) + "   ->   s"+ str(x+1) +":"  + str(si[x])

 print ("********************************************")

 print "Statistics of service time = " + str(Stsi)
 print "Statistics of arrival time = " + str(Stai)

