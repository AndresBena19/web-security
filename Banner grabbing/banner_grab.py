
#!/usr/bin/python
import socket
import select
import sys

if len(sys.argv) != 4:
 print "Usage - ./banner_grab.py [Target-IP] [First Port] [Last Port]"
 print "Example - ./banner_grab.py 10.0.0.5 1 100"
 print "Example will grab banners for TCP ports 1 through 100 on 10.0.0.5"
 sys.exit()
    
ip = sys.argv[1]
start = int(sys.argv[2])
end = int(sys.argv[3])

for port in range(start,end):
   try:
    bangrab = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    bangrab.connect((ip, port))
    ready = select.select([bangrab],[],[],1) #Usando el objeto select podremos determinar si en la respuesta se encuentra algo legibel
					     #ya que existen servicios que se encuentran corriendo, pero no ofrecen un bannerde conexion
					     #este objeto necesita de 4 argumentos, " a read list, a write list, an exception list, and an integer value"
					     #en este caso solo nos interesa el  argumento de  lectura, los demas los dejamos vacios y el valor entero en 1, que  define el numero 
					     #de segundos en espera, para la conexion *timeout* 
					     #Nota= Select nos retorna un array
    if ready[0]: 
     print "TCP Port " + str(port) + " - " + bangrab.recv(4096)
     bangrab.close()
   except:
    pass
