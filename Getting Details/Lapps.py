import subprocess
from subprocess import Popen, PIPE
import sys


def check_execs(*progs):
    #We recieve a tupla for future funtional options
    for prog in progs:
        try:
            Popen([prog, '--help'], stdout=PIPE, stderr=PIPE)
        except OSError:
            msg = 'The {0} program is necessary to run this script'.format(prog)
            sys.exit(msg)
        else:
            Get_apps()


def Get_apps():
    #Finding the distributions type
    Host_info=subprocess.check_output(['uname -a'], shell=True)
    packets = open('Packets.txt', 'w+')
    temp = open('temp.txt', 'w+')
    apps = open('Apps.txt', 'w+')


    #getting the apps of the system
    if(Host_info.find("Debian")!= -1):
        subprocess.call(['dpkg', '-l'], stdout=temp)
        subprocess.call(['dpkg', '--get-selections'], stdout=packets)

        subprocess.Popen(('cut', '-c','1-65', 'temp.txt'), stdout=apps)
        subprocess.call(['rm', 'temp.txt'])






    else:
        if(Host_info.find("fedora")!= -1 ):
            subprocess.call(['rmp', '-qa'])




if __name__ == '__main__':
    #Checking
    check_execs('dpkg')
