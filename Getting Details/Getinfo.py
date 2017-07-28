#!/usr/bin/python
import os
import socket
if os.name != "nt":
    import fcntl
import struct
import argparse

def IP(inter):
 s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
 IP_ADDRESS = socket.inet_ntoa(fcntl.ioctl(s.fileno(), 0x8915,
 struct.pack('256s', inter[:15]))[20:24])
 return IP_ADDRESS

def MAC(inter):
 s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
 info = fcntl.ioctl(s.fileno(), 0x8927, struct.pack('256s', inter[:15]))
 MAC_ADDRESS = ''.join(['%02x:' % ord(char) for char in info[18:24]]) [:-1]
 return MAC_ADDRESS




if __name__=="__main__":
 parser = argparse.ArgumentParser(description="Script extraer la IP y MAC")
 parser.add_argument('-I', help="Interfaz", required=True, dest='INT')
 args = parser.parse_args()

 I = IP(args.INT)
 M = MAC(args.INT)
  
 hostname = "None"

 hostname = socket.gethostbyname(socket.gethostname())
 if hostname.startswith("127.") and os.name != "nt":
   hostdata = socket.gethostbyaddr(socket.gethostname())
   hostname = str(hostdata[1]).strip('[]')
 else:
   hostdata = socket.gethostbyaddr(socket.gethostname())
   hostname = str(socket.gethostname())
 
 print "The  interfaz " + args.INT +" have a IP:"+ I +" And MAC:" + M +" and the hostname is:"+ hostname 






