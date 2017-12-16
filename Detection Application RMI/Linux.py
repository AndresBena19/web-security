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
##########################################################
class Linux_app():

    def Detect_Linux(self):

        app = {}
        #Gettin the hostname of the host
        hostname = socket.gethostname()

        subprocess.Popen(['mkdir', hostname]) #On linux run well
        '''
        In some cases, the command mkdir, don't excute fast in the system and when the fuction scan, want to
        create a path on that directory, this does not exist yet
        '''
        time.sleep( 3 )

        #Finding the distributions type
        Host_info = subprocess.check_output(['uname -a'], shell=True)
        #packets = open('Packets.txt', 'w+')
        pathA = socket.gethostname() + '/Apps.txt'
        apps = open(pathA, 'w+')

        #getting the apps of the system
        if(Host_info.find("Debian")!= -1):

            sh = "-f=${Package} ${Version}\n"
            subprocess.call([ 'dpkg-query', '-W', sh ], stdout=apps)

            print "[+] the application analysis finished"


        else:
            if(Host_info.find("fedora")!= -1 ):
                subprocess.call(['rmp', '-qa'])


        fh = open(pathA, 'r')
        for line in fh:
            linea = line.split(' ')
            app[linea[0]]=linea[1]
        fh.close()
        subprocess.Popen(['rm','-r', hostname])
        return app, hostname
