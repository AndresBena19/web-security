#!/usr/bin/python


def Inventary(di):
 i=0
 S=200
 s=25
 Li=[200]
 Oi=[]
<<<<<<< HEAD

 while(i!=101): 
=======
 
 while(i!=101):
  
>>>>>>> 4ada9ba84478f6896ac78acf96a5ec44ce803fd8
  i=i+1 
  if(Li[i-1]< s):
      Oi.insert(i-1,S-Li[i-1])

  else:
     Oi.insert(i-1, 0)
  DI=di[i]
  Li.insert(i, Li[i-1]+Oi[i-1]-DI)
 
 Oi.insert(i-1,S-Li[i])
 print  Oi[i]
 print i 
 Li[i]=S
 
 return Li,Oi,i  


def Promedio(Lista,N):
 Acum=0.0
 for x in range(0, len(Lista)):
    Acum=Acum+Lista[x]
 Prom=Acum/N
 return Prom,Acum


def AfterReview(Li,Oi):
  L=[]
  i=0
<<<<<<< HEAD
  while(i!=101):
=======
  while(i!=len(Li)):
>>>>>>> 4ada9ba84478f6896ac78acf96a5ec44ce803fd8
   i=i+1
   L.insert(i-1, Li[i-1]+Oi[i-1])
  return L



if __name__ == "__main__":

<<<<<<< HEAD
 di=[0,20,45,20,30,45,25,45,40,30,40,30,40,15,40,20,40,30,45,40,15,15,30,25,30,25,45,40,35,25,40,20,15,30,45,30,35,35,20,40,30,45,20,40,35,45,30,20,30,45,35,45,25,25,40,25,35,25,15,35,45,40,20,30,30,25,30,35,15,20,35,20,15,25,45,20,20,15,15,15,15,40,20,40,25,20,35,40,25,15,45,40,20,20,15,15,45,35,40,20,30,0] 
=======
 di=[0,20,45,20,30,45,25,45,40,30,40,30,40,15,40,20,40,30,45,40,15,15,30,25,30,25,45,40,35,25,40,20,15,30,45,30,35,35,20,40,30,45,20,40,35,45,30,20,30,45,35,45,25,25,40,25,35,25,15,35,45,40,20,30,30,25,30,35,15,20,35,20,15,25,45,20,20,15,15,15,15,40,20,40,25,20,35,40,25,15,45,40,20,20,15,15,45,35,40,20,30,0]
>>>>>>> 4ada9ba84478f6896ac78acf96a5ec44ce803fd8
 Li=[]
 Oi=[]
 L=[]
 Lmas=[]
 Lmenos=[]

 Li, Oi,i = Inventary(di)
 L = AfterReview(Li,Oi)

 print "************************************************************"
 print "Time   /   Demand   / Inventory  / Orders / Inventory after review"
 for x in range(101):
   print  str(x) + "       ->    di:" + str(di[x]) + "   ->   Li:" + str(Li[x]) + "   ->   Oi:" + str(Oi[x]) + "  ->  L':"+ str(L[x])
 print "************************************************************"
 print  "n" + "       ->    di:" + str(di[i]) + "   ->   Li:" + str(Li[i]) + "   ->   Oi:" + str(Oi[i]) + "  ->  L':"+ str(L[x])
 print "************************************************************"


 St,Acum = Promedio(di,100)
 SO = Promedio(Oi,100)
 SL =Promedio(Li,100)

 print "Average Demand (d)= " + str(St)
 print "Average of sorted items (o ) = " + str(SO[0])
 print "************************************************************"
 print "d = o = " + str(int(Acum)) + "/100 = " + str(SO[0])+ " items per time interval"
 print "************************************************************"
<<<<<<< HEAD
 print "Average of sorted items (Li) = " + str(SL[0])
 print "************************************************************"
 print "Operating cost"
 print " "

 U=0.0
 for x in range(0, 101):
    if(Oi[x]>0):
     U=U+1 
 Up=U/100
 print "Average setup cost  (u) :" + str(Up)

 p=0
 while(p!=100):
   p=p+1
   if(di[p]<=L[p-1]):
     Lmas.insert(p-1, L[p-1]-0.5*di[p])
   else:
     Lmas.insert(p-1, (L[p-1]*L[p-1])/(2.0*di[p]))
     Lmenos.insert(p-1,((di[p]-L[p-1])*(di[p]-L[p-1]))/(2.0*di[p]))

 SLmas = Promedio(Lmas,100)
 
 SLmenos = Promedio(Lmenos,100)
 print "Average holding level (L+) :" +  str(SLmas[0])
=======
 print "Average of sorted items (L ) = " + str(SL[0])
 print "************************************************************"
 print "Operating cost"

 U=0.0
 for x in range(0, 101):
    if(Oi[x]!=0):
     U=U+1
 Up=U/100
 print "Average setup cost  (u ) :" + str(Up)

 p=0
 while(p!=101):
   p=p+1
   Lmas.insert(p-1, ((L[p-1])**2)/2*di[p])

 k=0
 while(k!=101):
   k=k+1
   Lmenos.insert(k-1,(di[k]-L[k-1])**2/2*di[k])

 SLmas = Promedio(Lmas,100)
 SLmenos = Promedio(Lmenos,100)


 print "Average holding level (L+) :" + str(SLmas[0])
>>>>>>> 4ada9ba84478f6896ac78acf96a5ec44ce803fd8
 print "Average shortage level (L-) :" + str(SLmenos[0])
 print "Time-average inventory(L) :" + str(SLmas[0]-SLmenos[0]) 


 A= 5000*SO[0]
 B= 20000*Up
 C= 500*SLmas[0]
 D= 3000*SLmenos[0]
 print "***----****----****----*****----******----****---*****"
<<<<<<< HEAD
 print "item cost:"+ str(int(A)) + " per week"
 print "setup cost:"+ str(int(B)) + " per week"
 print "holding cost:"+ str(int(C)) + " per week"
 print "shortage cost:" +str(int(D)) + " per week"
 print " "
 print "Average dependent cost:" + str(int(A+B+C+D)) 

=======
 print "item cost:"+ str(A) + " per week"
 print "setup cost:"+ str(B) + " per week"
 print "holding cost:"+ str(C) + " per week"
 print "shortage cost:" +str(D) + " per week"
 
 print "Average dependent cost:" + str(A+B+C+D) 
>>>>>>> 4ada9ba84478f6896ac78acf96a5ec44ce803fd8
