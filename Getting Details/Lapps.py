'''
Author: Xion security
Date: March 2017
Name: RunAP.py
Purpose: To scan the host and his local network with the main  purpuse to find the install aplication's and service running

Copyright (c) 2017, Xion security All rights reserved.

Redistribution and use in source and binary forms, with or without modification, 
are permitted provided that the following conditions are met: * Redistributions 
of source code must retain the above copyright notice, this list of conditions and 
the following disclaimer. * Redistributions in binary form must reproduce the above 
copyright notice, this list of conditions and the following disclaimer in the 
documentation and/or other materials provided with the distribution. * Neither the 
name of the nor the names of its contributors may be used to endorse or promote 
products derived from this software without specific prior written permission.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS 
"AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, 
THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE 
DISCLAIMED. IN NO EVENT SHALL CHRISTOPHER DUFFY BE LIABLE FOR ANY DIRECT, INDIRECT, 
INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, 
PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS 
INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT 
LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE 
OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
'''
try:
    import subprocess
    from subprocess import Popen, PIPE
except ImportError:
    print ("[!] You don't have subprocess library installed")
    rp = raw_input('Do you want to install subprocess library (S/N)')
    if(rp=="S" or rp=="s"):
        subprocess.call(['pip install netifaces'], shell=True)
try:
    import sys
except ImportError:
    print ("[!] You don't have sys library installed")
    rp = raw_input('Do you want to install sys library (S/N)')
    if(rp=="S" or rp=="s"):
        subprocess.call(['pip install sys'], shell=True)
try:
    import platform
except ImportError:
    print ("[!] You don't have platform library installed")
    rp = raw_input('Do you want to install platform library (S/N)')
    if(rp=="S" or rp=="s"):
        subprocess.call(['pip install platform'], shell=True)

if((platform.system())=='Windows'):
    try:
        import _winreg
    except ImportError:
        print ("[!] You don't have winreg library installed")
        rp = raw_input('Do you want to install platform library (S/N)')
        if(rp=="S" or rp=="s"):
            subprocess.call(['pip install winreg'], shell=True)
try:
    import errno
except ImportError:
    print ("[!] You don't have errno library installed")
    rp = raw_input('Do you want to install errno library (S/N)')
    if(rp=="S" or rp=="s"):
        subprocess.call(['pip install errno'], shell=True)
try:
    import netifaces
    from netifaces import interfaces, ifaddresses, AF_INET
except ImportError:
    print ("[!] You don't have netifaces library installed")
    rp = raw_input('Do you want to install netifaces library (S/N)')
    if(rp=="S" or rp=="s"):
        subprocess.Popen(['pip',  'install', 'netifaces'], shell=True)
try:
    import unicodedata
except ImportError:
    print ("[!] You don't have nunicodedata library installed")
    rp = raw_input("Do you want to install netifaces library (S/N)")
    if(rp=='S' or rp =='s'):
        subprocess.call(['pip install unicodedata'], shell=True)
try:
    import threading
except ImportError:

    print ("[!] You don't have threading library installed")
    rp = raw_input('Do you want to install threading library (S/N)')
    if(rp=="S" or rp=="s"):
        subprocess.call(['pip install threading'], shell=True)
try:
    from nmap import *
except ImportError:
    print ("[!] You don't have nmap library installed")
    rp = raw_input("Do you want to install netifaces library (S/N)")
    if(rp=="S" or rp=="s"):
        subprocess.Popen(['pip', 'install', 'python-nmap'], shell=True)
try:
    import socket
except ImportError:
    print ("[!] You don't have socket library installed")
    rp = raw_input("Do you want to install socket library (S/N)")
    if(rp=="S" or rp=="s"):
        subprocess.call(['pip install socket'], shell=True)





#Detecting the necesary packets installed on the host
def check_execs(*progs):
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
            Get_apps()


def Get_apps():
    #Finding the distributions type
    Host_info=subprocess.check_output(['uname -a'], shell=True)
    #packets = open('Packets.txt', 'w+')

    path =  socket.gethostname() + '/temp.txt'
    pathA = socket.gethostname() + '/Apps.txt'

    temp = open(path , 'w+')
    apps = open(pathA, 'w+')

    #getting the apps of the system
    if(Host_info.find("Debian")!= -1):
        subprocess.call(['dpkg', '-l'], stdout=temp)
        #subprocess.call(['dpkg', '--get-selections'], stdout=packets)
        subprocess.Popen(('cut', '-c','1-65', path), stdout=apps)
        subprocess.call(['rm', path])

        print "[+] the application analysis finished"
        print "[+] find the file here " + pathA + "\n"



    else:
        if(Host_info.find("fedora")!= -1 ):
            subprocess.call(['rmp', '-qa'])



#Getting the apps installed on the host, in the case that the system os is windows
def apps_installed():
	# Open the key and return the handle object.
	hKey = _winreg.OpenKey(_winreg.HKEY_LOCAL_MACHINE, "SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall")

	for i in xrange(0, _winreg.QueryInfoKey(hKey)[0]):
		SubKeyName = _winreg.EnumKey(hKey, i)
		OpenSubKey= _winreg.OpenKey(hKey,SubKeyName)
		try:
			appName = (_winreg.QueryValueEx(OpenSubKey, 'DisplayName')[0]).encode("utf-8")
			appVersion = (_winreg.QueryValueEx(OpenSubKey, 'DisplayVersion')[0]).encode("utf-8")
			save_installed_apps(appName + ' ' + '-'*10 + ' ' + appVersion + '\n')
		except OSError as e:
			if e.errno == errno.ENOENT:
				# Display doesn't exist in this key
				pass
		OpenSubKey.Close()

# We create a file to save the apps installed
def save_installed_apps(app):
 path = socket.gethostname() + '/Apps.txt'
 with open(path,'a+') as f:
        f.write(app)
 



#Detecting the os tha is running on the host
def Detect_Os():
     system = platform.system()
     return system


#We use this funtion to find the interfaces on the host and his ip's
def Services():
    ip={}
    #we march  one by one the ip's each on interfaces
    for ifaceName in interfaces():
        addresses = [i['addr'] for i in ifaddresses(ifaceName).setdefault(AF_INET, [{'addr':'NONE'}] )]
        #We just save the valid ip on the dictionary
        if(addresses[0]!="NONE"):
            ip[ifaceName]=addresses[0]
    #retunr the dictionary with the ip
    return ip

#Usign nmap we scan the ips on our diferents interfeaces
def scan(key, start, end):
    
    scanner = nmap.PortScanner()
    #We gonna scan all the known port for all the ip found on the host
    for port in range(start, end):
        temp = scanner.scan(key, str(port))
        temp2 = temp['scan']
        print key, port
        
        #We insure that the dictionaris is not empty
        if(len(temp2)>0):
            temp3 = temp2[key]
            temp4 = temp3['tcp']
            temp5 = temp4[port]
            #we insure that the key in te result dictionari is not empty
            if(temp5['product']!=''):
                
                #concatenate the significant information
                id_Service = temp5['product'] + " " + temp5['version']  + "............ " + key +" "+ str(port) + "\n"
                #We just save valid information :v
                path = socket.gethostname() + "/services.txt"
                print id_Service
                with open(path, "a") as archivo:
                            archivo.write(id_Service)





#This class use his method run, to call Services with a specific range of port
class myThread (threading.Thread):
    #Definition of the constructor
    def __init__(self,key,st,en):
        threading.Thread.__init__(self)
        self.st = st
        self.en = en
        self.key = key
    #Method run
    def run(self):
        scan(self.key, self.st,self.en)


def Detect_Services():
    #ip = { 'eth0': '192.168.1.1', 'eth1': '192.168.1.2', 'eth2': '192.168.1.4'}
    ip = Services()
    #We gonna march all the key of the dictinary using threads
    for key in ip:
        #We select 1024 becouse is the range of the known port's
        total_ip = 1
        # number of ip handled by one thread
        tn = 4
        total_thread = total_ip/tn
        total_thread=total_thread+1

        #The  number of port that we gonna analize
        start  = 137
        end =  140

        threads= []
        #We gonna try to find the exception for the future
        try:
            #We began with a cicle until total_threads that is the division between number of port and the threads proposed
                 for i in xrange(total_thread):
                     #we begin taking a part o the portion of port's
                     en = start + tn
                     #In the case that the portion of port be greater that the end, the portion will become the end
                     #That's becouse  usually the total number of port can not be divided exactly in the same number  of proposed threads
                     if(en > end):
                         en = end
                     #pass the parameter  on the class
                     thread = myThread(ip[key],start ,en)
                     #start the thread
                     thread.start()
                     #Adding the threads in the list
                     threads.append(thread)
                     #the start now gonna become the end, becouse the function mythread must be call, with another portion or port's
                     start  = en
       #In case that and exception occurs
        except:
          print "Error: unable to start thread"

        print "[+] Number of Threads active:  " + str(threading.activeCount()) + "  analizing " + str(unicodedata.normalize('NFKD', ip[key]).encode('ascii','ignore'))

        #the threads are activate one by one
        for t in threads:
         t.join()




if __name__ == '__main__':

    #Gettin the hostname of the host
    hostname = socket.gethostname()
    #Create de directory where the information gonna save_installed_apps
    subprocess.call(['mkdir', hostname], shell=True)
    #We begin detecting what is the system operation on the host
    if(Detect_Os()== 'Linux'):
        print "[*] Starting the application analysis on " + Detect_Os()
        #Checking installed packets
        check_execs('dpkg')
        print "[*] Starting the service analysis on " + Detect_Os()
        #We began to detect de services tha is running
        Detect_Services()
        print "[+] find the file in " + socket.gethostname() + "/services.txt"
    else:
        #In case that de SO be windows
        if(Detect_Os()=='Windows'):
            print "[*] Starting the application analysis on " + Detect_Os()
            #we begin detection the application's install in the host
            apps_installed()
            print "[+] the application analysis finished"
            print "[+] find the file here " + socket.gethostname() + '/Apps.txt' + "\n"
            print "[*] Starting the service analysis on " + Detect_Os()
            #We began to detect de services tha is running
            Detect_Services()
            print "[+] find the file in " + socket.gethostname() + "/services.txt"
        else:
            #In case that de SO be windows
            if(Detect_Os()=='darwin'):
                #in progress :V
                pass
