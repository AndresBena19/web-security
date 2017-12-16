
#########################################################
import subprocess
from subprocess import Popen, PIPE
import sys
import platform

if((platform.system())=='Windows'):
    import _winreg

import errno
import netifaces
from netifaces import interfaces, ifaddresses, AF_INET
import unicodedata
import threading
from nmap import *
import socket
import time
##########################################################
import Pyro4


class Detect_info():
    #Detecting the os tha is running on the host
    def Detect_Os(self):
         self.system = platform.system()
         return self.system

     #Detecting the necesary packets installed on the host
    def check_execs(self,*progs):
         #We recieve a tupla for future funtional options
         for prog in progs:
             try:
                 #If the packet is install, he should be deploy information about him
                 Popen([prog, '--help'], stdout=PIPE, stderr=PIPE)
             #In case that and exception ocurrs
             except OSError:
                 msg = 'The {0} program is necessary to run this script'.format(prog)
                 sys.exit(msg)
             #In case that the exception don't activate, the get_apps fuction is call
             else:
                 return True
    #We use this funtion to find the interfaces on the host and his ip's
    def Address(self):
        ip={}
        #we march  one by one the ip's each on interfaces
        for ifaceName in interfaces():
            addresses = [i['addr'] for i in ifaddresses(ifaceName).setdefault(AF_INET, [{'addr':'NONE'}] )]
            #We just save the valid ip on the dictionary
            if(addresses[0]!="NONE"):
                ip[ifaceName]=addresses[0]
        #retunr the dictionary with the ip
        return ip
