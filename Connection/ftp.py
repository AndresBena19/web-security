#! /usr/bin/python

import socket


socket.setdefaulttimeout(2)

client = socket.socket()

client.connect(("ftp.serxion.com", 21))


request = client.recv(2048)

print request
