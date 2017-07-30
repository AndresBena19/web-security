#!/usr/bin/python

from scapy.all import *
import argparse
import threading
import collections
import platform
import threading
from datetime import datetime


def SYN(start, end): 
 for port in range(start,end):
  ans = sr1(IP(dst=args.USER)/TCP(dport=port),timeout=1,verbose=0) 
 #La cabecera TCP, trae por defecto el flag S activo, para iniciar la sincronizacion
  if ans == None:
   pass
  else:

   if int(ans[TCP].flags) == 18:
    #print port
    dic[port] = port 
   else:
    pass

class myThread (threading.Thread):
 def __init__(self,st,en):
  threading.Thread.__init__(self)
  self.st = st
  self.en = en
 def run(self):
  SYN(self.st,self.en)




if __name__ == "__main__":


 t1= datetime.now()
 dic = collections.OrderedDict()
 parser = argparse.ArgumentParser(description="Escaneo tipo SYN con threading")
 parser.add_argument('-P', '--IP_USER',metavar="IPUSER", help="IP de la victima", required=True, dest='USER')
 parser.add_argument('-S', '--PT_START',metavar="PORTST", help="Puerto de inicio", required=True, dest='ST')
 parser.add_argument('-E', '--PT_END',metavar="PORTEND", help="Puerto final", required=True, dest='END')

 args = parser.parse_args()

 ''' Section 4 '''

 total_ip = (int(args.END)) - (int(args.ST))
 print  total_ip 
 tn =20 # number of ip handled by one thread
 total_thread = total_ip/tn
 print total_thread
 total_thread=total_thread+1
 print total_thread
 start  = int(args.ST) 
 end =  int(args.END) 
 threads= []
 try:
  for i in xrange(total_thread):
   en = start + tn
   print en
   if(en > end):
    en = end
   thread = myThread(start ,en)
   thread.start()
   threads.append(thread) 
   start  = en
 except:
   print "Error: unable to start thread"
 
 print "\tNumber of Threads active:", threading.activeCount()
 for t in threads:
  t.join()
 print "Exiting Main Thread"
 dict = collections.OrderedDict(sorted(dic.items()))
 for key in dict:
  print dict[key],"-->" "Live"
 t2= datetime.now()
 total =t2-t1
 print "scanning complete in " , total
