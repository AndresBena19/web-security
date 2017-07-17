#!/usr/bin/python

import socket

tcpSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcpSocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

tcpSocket.bind(("0.0.0.0", 8000))
tcpSocket.listen(2)

print "Waiting a client"
(client, (ip, sock)) = tcpSocket.accept()

print "Conection detected from ip =", ip
print "start"

data = " basura"

while len(data):
 data = client.recv(2048)
 print "Send to client", data
 client.send(data)

print "Closing conection"
client.close()
