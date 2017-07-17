#! /usr/bin/python


import socket

if __name__ == '__main__':
   ip = raw_input('Ingrese la IP/URL=')
   ipurl = socket.gethostbyname(ip)
   print "Comenzando escaneo a la direccion:", ipurl;

   for ports in range(1, 1024):
     client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
     request = client.connect_ex((ipurl, ports))
     if (request==0):
       print "Port:", ports, "open";
       client.close()
     else:
       print "Port:", ports, "open";


