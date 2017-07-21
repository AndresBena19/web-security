#!/usr/bin/python

import logging
logging.getLogger("scapy.runtime").setLevel(logging.ERROR)
from scapy.all import *

if len(sys.argv) != 2:
 print "Usage - ./Scapy_layer3.py [/24 network address]"
 print "Example - ./Scapy_layer3. 172.16.36.0"
 print "Example will perform an ICMP scan of the 172.16.36.0/24 range"
 sys.exit()
    
address = str(sys.argv[1])
prefix = address.split('.')[0] + '.' + address.split('.')[1] + '.' + address.split('.')[2] + '.'

for addr in range(1,254):
 answer=sr1(ARP(pdst=prefix+str(addr)),timeout=1,verbose=0)
 if answer == None:
  pass
 else:  #Si nuestra respuesta contiene algo, seguramente  es la MAC en el campo hwdst  de la cabecera  ARP, de lo contrario, ninguna respues hubiese sido  detecta despues de  la difusion broadcast
  print prefix+str(addr)
