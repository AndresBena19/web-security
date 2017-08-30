def Inventary(di):
 i=0
 S=200
 s=25
 Li=[200]
 Oi=[]

 while(i!=101): 
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
  while(i!=101):
   i=i+1
   L.insert(i-1, Li[i-1]+Oi[i-1])
  return L



if __name__ == "__main__":

 di=[0,20,45,20,30,45,25,45,40,30,40,30,40,15,40,20,40,30,45,40,15,15,30,25,30,25,45,40,35,25,40,20,15,30
,45,30,35,35,20,40,30,45,20,40,35,45,30,20,30,45
,35,45,25,25,40,25,35,25,15,35,
45,40,20,30,30,25,30,35,15,20,35,20,15,25,45,20,20,15,15,15,15,40,20,40,25,20,35,40,25,15,45,40,20,20,15,15,45,35,40,20,30,0] 

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
 print "Average order (o ) = " + str(SO[0])
 print "************************************************************"
 print "d = o = " + str(int(Acum)) + "/100 = " + str(SO[0])+ " items per time interval"
 print "************************************************************"
 print "Average of inventory level (Li) = " + str(SL[0])
 print "************************************************************"
 print "Operating cost"
 print " "

 U=0.0
 for x in range(0, 101):
    if(Oi[x]>0):
     U=U+1 
 Up=U/100
 print "Average order frequency  (u) :" + str(Up)

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
 print "Average shortage level (L-) :" + str(SLmenos[0])
 print "Time-average inventory(L) :" + str((SLmas[0]-SLmenos[0])/100) 


 A= 5000*SO[0]
 B= 20000*Up
 C= 500*SLmas[0]
 D= 3000*SLmenos[0]
 print "***----****----****----*****----******----****---*****"
 print "average item cost:"+ str(int(A)) + " per week"
 print "average setup cost:"+ str(int(B)) 
 print "average holding cost:"+ str(int(C)) + " per week"
 print "average shortage cost:" +str(int(D)) + " per week"
 print " "
 print "Average operating cost:" + str(int(A+B+C+D))
 print "Average dependent cost:" + str(int(B+C+D)) 

'''
************************************************************
Time   /   Demand   / Inventory  / Orders / Inventory after review
0       ->    di:0   ->   Li:200   ->   Oi:0  ->  L':200
1       ->    di:20   ->   Li:180   ->   Oi:0  ->  L':180
2       ->    di:45   ->   Li:135   ->   Oi:0  ->  L':135
3       ->    di:20   ->   Li:115   ->   Oi:0  ->  L':115
4       ->    di:30   ->   Li:85   ->   Oi:0  ->  L':85
5       ->    di:45   ->   Li:40   ->   Oi:0  ->  L':40
6       ->    di:25   ->   Li:15   ->   Oi:185  ->  L':200
7       ->    di:45   ->   Li:155   ->   Oi:0  ->  L':155
8       ->    di:40   ->   Li:115   ->   Oi:0  ->  L':115
9       ->    di:30   ->   Li:85   ->   Oi:0  ->  L':85
10       ->    di:40   ->   Li:45   ->   Oi:0  ->  L':45
11       ->    di:30   ->   Li:15   ->   Oi:185  ->  L':200
12       ->    di:40   ->   Li:160   ->   Oi:0  ->  L':160
13       ->    di:15   ->   Li:145   ->   Oi:0  ->  L':145
14       ->    di:40   ->   Li:105   ->   Oi:0  ->  L':105
15       ->    di:20   ->   Li:85   ->   Oi:0  ->  L':85
16       ->    di:40   ->   Li:45   ->   Oi:0  ->  L':45
17       ->    di:30   ->   Li:15   ->   Oi:185  ->  L':200
18       ->    di:45   ->   Li:155   ->   Oi:0  ->  L':155
19       ->    di:40   ->   Li:115   ->   Oi:0  ->  L':115
20       ->    di:15   ->   Li:100   ->   Oi:0  ->  L':100
21       ->    di:15   ->   Li:85   ->   Oi:0  ->  L':85
22       ->    di:30   ->   Li:55   ->   Oi:0  ->  L':55
23       ->    di:25   ->   Li:30   ->   Oi:0  ->  L':30
24       ->    di:30   ->   Li:0   ->   Oi:200  ->  L':200
25       ->    di:25   ->   Li:175   ->   Oi:0  ->  L':175
26       ->    di:45   ->   Li:130   ->   Oi:0  ->  L':130
27       ->    di:40   ->   Li:90   ->   Oi:0  ->  L':90
28       ->    di:35   ->   Li:55   ->   Oi:0  ->  L':55
29       ->    di:25   ->   Li:30   ->   Oi:0  ->  L':30
30       ->    di:40   ->   Li:-10   ->   Oi:210  ->  L':200
31       ->    di:20   ->   Li:180   ->   Oi:0  ->  L':180
32       ->    di:15   ->   Li:165   ->   Oi:0  ->  L':165
33       ->    di:30   ->   Li:135   ->   Oi:0  ->  L':135
34       ->    di:45   ->   Li:90   ->   Oi:0  ->  L':90
35       ->    di:30   ->   Li:60   ->   Oi:0  ->  L':60
36       ->    di:35   ->   Li:25   ->   Oi:0  ->  L':25
37       ->    di:35   ->   Li:-10   ->   Oi:210  ->  L':200
38       ->    di:20   ->   Li:180   ->   Oi:0  ->  L':180
39       ->    di:40   ->   Li:140   ->   Oi:0  ->  L':140
40       ->    di:30   ->   Li:110   ->   Oi:0  ->  L':110
41       ->    di:45   ->   Li:65   ->   Oi:0  ->  L':65
42       ->    di:20   ->   Li:45   ->   Oi:0  ->  L':45
43       ->    di:40   ->   Li:5   ->   Oi:195  ->  L':200
44       ->    di:35   ->   Li:165   ->   Oi:0  ->  L':165
45       ->    di:45   ->   Li:120   ->   Oi:0  ->  L':120
46       ->    di:30   ->   Li:90   ->   Oi:0  ->  L':90
47       ->    di:20   ->   Li:70   ->   Oi:0  ->  L':70
48       ->    di:30   ->   Li:40   ->   Oi:0  ->  L':40
49       ->    di:45   ->   Li:-5   ->   Oi:205  ->  L':200
50       ->    di:35   ->   Li:165   ->   Oi:0  ->  L':165
51       ->    di:45   ->   Li:120   ->   Oi:0  ->  L':120
52       ->    di:25   ->   Li:95   ->   Oi:0  ->  L':95
53       ->    di:25   ->   Li:70   ->   Oi:0  ->  L':70
54       ->    di:40   ->   Li:30   ->   Oi:0  ->  L':30
55       ->    di:25   ->   Li:5   ->   Oi:195  ->  L':200
56       ->    di:35   ->   Li:165   ->   Oi:0  ->  L':165
57       ->    di:25   ->   Li:140   ->   Oi:0  ->  L':140
58       ->    di:15   ->   Li:125   ->   Oi:0  ->  L':125
59       ->    di:35   ->   Li:90   ->   Oi:0  ->  L':90
60       ->    di:45   ->   Li:45   ->   Oi:0  ->  L':45
61       ->    di:40   ->   Li:5   ->   Oi:195  ->  L':200
62       ->    di:20   ->   Li:180   ->   Oi:0  ->  L':180
63       ->    di:30   ->   Li:150   ->   Oi:0  ->  L':150
64       ->    di:30   ->   Li:120   ->   Oi:0  ->  L':120
65       ->    di:25   ->   Li:95   ->   Oi:0  ->  L':95
66       ->    di:30   ->   Li:65   ->   Oi:0  ->  L':65
67       ->    di:35   ->   Li:30   ->   Oi:0  ->  L':30
68       ->    di:15   ->   Li:15   ->   Oi:185  ->  L':200
69       ->    di:20   ->   Li:180   ->   Oi:0  ->  L':180
70       ->    di:35   ->   Li:145   ->   Oi:0  ->  L':145
71       ->    di:20   ->   Li:125   ->   Oi:0  ->  L':125
72       ->    di:15   ->   Li:110   ->   Oi:0  ->  L':110
73       ->    di:25   ->   Li:85   ->   Oi:0  ->  L':85
74       ->    di:45   ->   Li:40   ->   Oi:0  ->  L':40
75       ->    di:20   ->   Li:20   ->   Oi:180  ->  L':200
76       ->    di:20   ->   Li:180   ->   Oi:0  ->  L':180
77       ->    di:15   ->   Li:165   ->   Oi:0  ->  L':165
78       ->    di:15   ->   Li:150   ->   Oi:0  ->  L':150
79       ->    di:15   ->   Li:135   ->   Oi:0  ->  L':135
80       ->    di:15   ->   Li:120   ->   Oi:0  ->  L':120
81       ->    di:40   ->   Li:80   ->   Oi:0  ->  L':80
82       ->    di:20   ->   Li:60   ->   Oi:0  ->  L':60
83       ->    di:40   ->   Li:20   ->   Oi:180  ->  L':200
84       ->    di:25   ->   Li:175   ->   Oi:0  ->  L':175
85       ->    di:20   ->   Li:155   ->   Oi:0  ->  L':155
86       ->    di:35   ->   Li:120   ->   Oi:0  ->  L':120
87       ->    di:40   ->   Li:80   ->   Oi:0  ->  L':80
88       ->    di:25   ->   Li:55   ->   Oi:0  ->  L':55
89       ->    di:15   ->   Li:40   ->   Oi:0  ->  L':40
90       ->    di:45   ->   Li:-5   ->   Oi:205  ->  L':200
91       ->    di:40   ->   Li:160   ->   Oi:0  ->  L':160
92       ->    di:20   ->   Li:140   ->   Oi:0  ->  L':140
93       ->    di:20   ->   Li:120   ->   Oi:0  ->  L':120
94       ->    di:15   ->   Li:105   ->   Oi:0  ->  L':105
95       ->    di:15   ->   Li:90   ->   Oi:0  ->  L':90
96       ->    di:45   ->   Li:45   ->   Oi:0  ->  L':45
97       ->    di:35   ->   Li:10   ->   Oi:190  ->  L':200
98       ->    di:40   ->   Li:160   ->   Oi:0  ->  L':160
99       ->    di:20   ->   Li:140   ->   Oi:0  ->  L':140
100       ->    di:30   ->   Li:110   ->   Oi:90  ->  L':200
************************************************************
n       ->    di:0   ->   Li:200   ->   Oi:0  ->  L':200
************************************************************
Average Demand (d)= 29.95
Average order (o ) = 29.95
************************************************************
d = o = 2995/100 = 29.95 items per time interval
************************************************************
Average of inventory level (Li) = 96.45
************************************************************
Operating cost
 
Average order frequency  (u) :0.16
Average holding level (L+) :107.45734127
Average shortage level (L-) :0.0323412698413
Time-average inventory(L) :1.07425
***----****----****----*****----******----****---*****
average item cost:149750 per week
average setup cost:3200
average holding cost:53728 per week
average shortage cost:97 per week
 
Average operating cost:206775
Average dependent cost:57025



'''
