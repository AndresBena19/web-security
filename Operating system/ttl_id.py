#!/usr/bin/python
from scapy.all import *
import logging
logging.getLogger("scapy.runtime").setLevel(logging.ERROR)
import sys

if len(sys.argv) != 2:
 print "Usage - ./ttl_id.py [IP Address]"
 print "Example - ./ttl_id.py 10.0.0.5"
 print "Example will perform ttl analysis to attempt to determine whether the system is Windows or Linux/Unix"
 sys.exit()

ip = sys.argv[1]
ans = sr1(IP(dst=str(ip))/ICMP(),timeout=1,verbose=0)

if ans == None:
 print "No response was returned"
elif int(ans[IP].ttl) <= 64: #Un comportamiento comun de los sistemas Lunix/unix, es que el valor  de TTL en la cabecera IP,varia entre 0 y 64, por ende es tomado por muchos escaneres como un indexado confiable para determinar el S.0 
 print "Host is Linux/Unix"
else:
 print "Host is Windows" #En windows el TTL varia entre 65  y 128
