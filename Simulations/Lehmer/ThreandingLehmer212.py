#!/usr/bin/python

import threading
import collections
import threading
from datetime import datetime
import fractions

def fullP(p,n):
 m=13
 for a in range (p,n):
  i=1
  x=a
  while(x!=1):
   if(fractions.gcd(i , m-1)==1):
     w=(a**i)%m
     print "full period multiplier:", w
   i=i+1
   x=(a*x)%m 

class myThread (threading.Thread):
 def __init__(self,begin,final):
  threading.Thread.__init__(self)
  self.begin = begin
  self.final=final
 def run(self):
  fullP(self.begin,self.final)


if __name__ == "__main__":
 
 begin=1
 final=13
 dict=[]

 t1= datetime.now()
 tn =5 
 total_thread = final/tn
 total_thread=total_thread+1 
 start  = begin
 end =  final
 
 threads= []
 
 try:
  for i in xrange(total_thread):
   en = start + tn
   if(en > end):
    en = end
   thread = myThread(start,en)
   thread.start()
   threads.append(thread) 
   start  = en
   
 except:
   print "Error: unable to start thread"
 
 print "\tNumber of Threads active:", threading.activeCount()
 
 for t in threads:
  t.join()
  
 

 t2= datetime.now()
 
 total =t2-t1
 print "scanning complete in " , total
