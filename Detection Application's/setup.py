import subprocess
import platform

'''
#In case that the host be windows, we gonna install winreg
if((platform.system())=='Windows'):
	subprocess.call(['pip install winreg'], shell=True)

#install the other packet's dependencies
subprocess.call(['pip', 'install', 'errno'], shell=True)
subprocess.call(['pip', 'install', 'netifaces'], shell=True)
subprocess.call(['pip', 'install', 'unicodedata'], shell=True)
subprocess.call(['pip', 'install', 'threading'], shell=True)
subprocess.call(['pip', 'install', 'python-nmap'], shell=True)
subprocess.call(['pip', 'install', 'socket'], shell=True)
subprocess.call(['pip', 'install', 'time'], shell=True)
'''
#execute the main aplication 
subprocess.call(['python', 'Lapps.py'])
