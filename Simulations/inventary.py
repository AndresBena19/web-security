
#!/usr/bin/python

S=60
s=20
di=[30,15,25,15,45,30,25,15,20,35,20,30,0]
Li=[60]
Oi=[]


i=0;

for i in range(len(di)):

    if(Li[i]< s):
      Oi.insert(i,S-Li[i])

    else:
     Oi.insert(i, 0)

    DI = di[i]

    Li.insert(i+1, Li[i]+Oi[i]-DI)

print "************************************************************"
print "Tiempo   /   Demanda   / Inventario  / Ordenes"
for x in range(13):
  print  str(x) + "       ->    di:" + str(di[x]) + "   ->   Li:" + str(Li[x]) + "   ->   Oi:" + str(Oi[x])

print "************************************************************"


Oi.insert(i,S-Li[i])

Li[i]=S
print  "n" + "       ->    di:" + str(di[i]) + "   ->   Li:" + str(Li[i]) + "   ->   Oi:" + str(Oi[i]) 

print "************************************************************"
PromedioDI=0.0;

for x in range(0, len(di)):
   PromedioDI=PromedioDI+di[x]


St=PromedioDI/12
print "Average Demand (d)= " + str(St)


PromedioOI=0.0;

for x in range(0, len(Oi)):
   PromedioOI=PromedioOI+Oi[x]

SO=PromedioDI/12
print "Average of sorted items (o) = " + str(SO)
print "************************************************************"
print "d = o = " + str(int(PromedioDI)) + "/12 = " + str(SO)+ " items per time interval"
print "************************************************************"

PromedioLI=0.0;

for x in range(0, len(Li)):
   PromedioLI=PromedioLI+Li[x]

SL=PromedioLI/12
print "Average of sorted items (L ) = " + str(SL)



U=0.0
for x in range(0, 13):
   if(Oi[x]!=0):
     U=U+1

Up=U/12

print "Average setup cost  (u) :" + str(Up)
