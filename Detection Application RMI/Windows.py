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

import Pyro4
##########################################################
from Detect_OS import *
##########################################################


class Windows_app():

    def Detect_windows(self):

        app = {}

        #Gettin the hostname of the host
        hostname = socket.gethostname()
        #We use socket, to extract de hostname and the ip on the interfaces
        Index = socket.gethostbyname_ex(socket.gethostname())
    	# Open the key and return the handle object.
    	hKey = _winreg.OpenKey(_winreg.HKEY_LOCAL_MACHINE, "SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall")

    	for i in xrange(0, _winreg.QueryInfoKey(hKey)[0]):
    		SubKeyName = _winreg.EnumKey(hKey, i)
    		OpenSubKey= _winreg.OpenKey(hKey,SubKeyName)
    		try:
    			appName = (_winreg.QueryValueEx(OpenSubKey, 'DisplayName')[0]).encode("utf-8")
    			appVersion = (_winreg.QueryValueEx(OpenSubKey, 'DisplayVersion')[0]).encode("utf-8")
    			app[appName]= appVersion
    		except OSError as e:
    			if e.errno == errno.ENOENT:
    				# Display doesn't exist in this key
    				pass
    		OpenSubKey.Close()
        return app, hostname
