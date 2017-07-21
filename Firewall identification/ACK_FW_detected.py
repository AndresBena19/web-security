#!/usr/bin/python
import sys
import logging
logging.getLogger("scapy.runtime").setLevel(logging.ERROR)


from scapy.all import *

if len(sys.argv) != 3:
 print "Usage - ./ACK_FW_detect.py [Target-IP] [Target Port]"
 print "Example - ./ACK_FW_detect.py 10.0.0.5 443"
 print "Example will determine if filtering exists on port 443 of
 host 10.0.0.5"
 sys.exit()

ip = sys.argv[1]
port = int(sys.argv[2])
ACK_response = sr1(IP(dst=ip)/TCP(dport=port,flags='A'),timeout=1,verbose=0)
SYN_response =sr1(IP(dst=ip)/TCP(dport=port,flags='S'),timeout=1,verbose=0)


if (ACK_response == None) and (SYN_response == None): #Si no se recibe respuesta en ninguno a ninguno de los  dos paquetes, es muy probable que el host este dowm
 print "Port is either unstatefully filtered or host is down"
elif ((ACK_response == None) or (SYN_response == None)) and not ((ACK_response ==None) and (SYN_response == None)): #En caso de que almenos  alguno  de los enviados hay recibido respuesta
 														    #podemos considerar  que el puerto se encuentra filtrado
 print "Stateful filtering in place" 
elif int(SYN_response[TCP].flags) == 18: #Si el valor del flag en al cabecera TCP es de 18, es decir SYN ACK, significa que el host respondio exitosamente, confirmando la sincronizacion de una conexion
 print "Port is unfiltered and open"     #por lo tanto consideramos que el puerto se encuentra abierto
elif int(SYN_response[TCP].flags) == 20: #Si el valor del flag en la cabecera TCP es de 20, es decir SYN RST, signiifica que el host respondio exitosamente, pero no quiere establecer una conexion
 print "Port is unfiltered and closed"   #por lo tanto consideramos que el puerto se encuentra cerrado
else:
 print "Unable to determine if the port is filtered" #Si nada d elo anterior fue confirmado, entonces no se puede  determinar si el puerto esta filtrado
