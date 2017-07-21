#!/usr/bin/python2.7

from scapy.all import *
import logging
import argparse
import sys

logging.getLogger("scapy.runtime").setLevel(logging.ERROR)

parser = argparse.ArgumentParser(description="Script para detectar el OS de un sistema")
parser.add_argument('ip', help="IP del Host el cual se examinara")

args = parser.parse_args()


ip = args.ip

ans = sr1(
			IP(dst=str(ip))/ICMP(),
			timeout=1,
			verbose=0
		)

if ans == None:
 print "No response was returned"
elif int(ans[IP].ttl) <= 64: #Un comportamiento comun de los sistemas Lunix/unix, es que el valor  de TTL en la cabecera IP,varia entre 0 y 64, por ende es tomado por muchos escaneres como un indexado confiable para determinar el S.0 
 print "Host is Linux/Unix"
else:
 print "Host is Windows" #En windows el TTL varia entre 65  y 128                                                
