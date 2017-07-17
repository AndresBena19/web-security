#! /usr/bin/python

import socket

host = 'savio.utbvirtual.edu.co'
port = 80

client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

client.connect((host, port))

client.send("GET / HTTP/1.1\r\n host: savio.utbvirtual.edu.co\r\n\r\n")

request = client.recv(2048)

print request
