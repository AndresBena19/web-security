#!/usr/bin/python

import threading
import collections
import threading
from datetime import datetime

def fullP(dict,cont,p,n):
 m=127
 for a in range (p,n):
  p=1
  x=a

  while(x!=1):
    p=p+1
    x=(a*x)%m
   
  if(p==m-1):
   dict.insert(cont,a)
   cont=cont+1
   
 return dict
class myThread (threading.Thread):
 def __init__(self,dict, cont, begin,final):
  threading.Thread.__init__(self)
  self.begin = begin
  self.final=final
  self.cont=cont
  self.dict=dict
 def run(self):
  fullP(self.dict,self.cont,self.begin,self.final)

if __name__ == "__main__":
 
 begin=1
 final=126
 dict=[]
 t1= datetime.now()
 tn =20
 total_thread = final/tn
 total_thread=total_thread+1 
 start  = begin
 end =  final
 threads= []
 
 try:
  for i in xrange(total_thread):
   cont=0
   en = start + tn
   if(en > end):
    en = end
   thread = myThread(dict, cont,start,en)
   thread.start()
   threads.append(thread) 
   start  = en
 except:
   print "Error: unable to start thread"
 
 print "\tNumber of Threads active:", threading.activeCount()
 
 for t in threads:
  t.join()
 

 full=[]
 orderfull=[] 

 print "full-period multiplayer:"
 for r in range(len(dict)):
   if(dict[r]!=None):
      full.insert(r,dict[r])
 
 orderfull= sorted(full)
 print orderfull

 t2= datetime.now()

 total =t2-t1
 print "Number of full period multiplier is:", len(orderfull)
 print  "numer of full period multiplier is:", cont
 print "scanning complete in " , total
