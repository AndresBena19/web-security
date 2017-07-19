#!/usr/bin/python


import logging
logging.getLogger("scapy.runtime").setLevel(logging.ERROR)
from scapy.all import *

SYN = IP(dst="172.16.36.135")/TCP(dport=80,flags='S')
print "-- SENT --"
SYN.display()

print "\n\n-- RECEIVED --"
response = sr1(SYN,timeout=1,verbose=0)
response.display()

if int(response[TCP].flags) == 18:
    
 print "\n\n-- SENT --"
 ACK = IP(dst="172.16.36.135")/TCP(dport=80,flags='A',ack=(response[TCP].seq + 1))
 response2 = sr1(ACK,timeout=1,verbose=0)
 ACK.display()
    
 print "\n\n-- RECEIVED --"
 response2.display()
    
else:
 print "SYN-ACK not returned"

#Para que la conexion sea completada con ayuda de scapy, se deben  bloquear
#el envio de paquetes RST por parte de nuestro sistema, para que en el momento
#de enviar el paque SYN y sea respondido con SYN-ACK, enviemos respectivamente 
#el paquete ACK de confirmacion y  no un RST por parte de nuestro sistema


#root@KaliLinux:~# iptables -A OUTPUT -p tcp --tcp-flags RST RST -d

#172.16.36.135 -j DROP

#root@KaliLinux:~# iptables --list

#Chain INPUT (policy ACCEPT)
#target prot opt source destination

#Chain FORWARD (policy ACCEPT)
#target prot opt source destination

#Chain OUTPUT (policy ACCEPT)

#target prot opt source destination
#DROP tcp -- anywhere 172.16.36.135 tcp
#flags:RST/RST

#Esta configuracion no es recomendada  para el uso normal de nuestro equipo
#ya que los paquetes RST desarrollan un trabajo importante, en la capa de red
