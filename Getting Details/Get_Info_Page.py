#!/usr/bin/python

import socket 
import argparse
 

def GetDirs(prefix):
 return dict( (getattr(socket, a), a)
  for a in dir(socket)
   if a.startswith(prefix))

proto_fam = GetDirs('AF_')
types = GetDirs('SOCK_')
protocols = GetDirs('IPPROTO_')


if __name__=="__main__":
 parser = argparse.ArgumentParser(description="Script extraer informacion")
 parser.add_argument('-D', help="Domain", required=True, dest='DOM')
 parser.add_argument('-P', help="Port", required=True, dest='PORT')

 args = parser.parse_args()


for res in socket.getaddrinfo(args.DOM, args.PORT):
 family, socktype, proto, canonname, sockaddr = res
 
 print 'Family :', proto_fam[family]
 print 'Type :', types[socktype]
 print 'Protocol :', protocols[proto]
 print 'Canonical name:', canonname
 print 'Socket address:', sockaddr
 print '-----------------------------------------'



