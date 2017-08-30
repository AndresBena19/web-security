#!/usr/bin/python
import threading
import collections
import threading
from datetime import datetime

def fullP(p,n):
 full=[]
 m=29
 pe=0
 for a in range(p,n):
  p=1
  x=a


  while(x!=1):
    p=p+1
    x=(a*x)%m

  if(p==m-1):
   print "Es un full-period multiplayer:"+str(a)
   full.insert(pe,a)
   pe=pe+1
 return full,pe

if __name__ == "__main__":

     t1= datetime.now()
     a,b=fullP(1,28)
     t2= datetime.now()
     total =t2-t1
     print "Numer of items:",b
     print "scanning complete in " , total
