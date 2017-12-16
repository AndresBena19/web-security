import Pyro4

from Detect_OS import *
from Windows import *
from Linux import *


@Pyro4.expose
class execution():

    def exec_app(self):
        Detect = Detect_info()
        #We instance a objetc from windows class
        Host_Windows = Windows_app()
        #We instance a objetc from linuxwindows class
        Host_Linux = Linux_app()

        if(Detect.Detect_Os() == 'Windows'):
                print "[*] Starting the application analysis on {}".format(Detect.Detect_Os())
                #we  begin detection the application's install in the host
                app, host = Host_Windows.Detect_windows()
                #We ganna replace all the special caracter here
                hostname = host.replace('-','')

        else:
            if(Detect.Detect_Os() == 'Linux'):

                print "[*] Starting the application analysis on {}".format(Detect.Detect_Os())
                #Checking installed packets
                if(Detect.check_execs('dpkg')):
                    print "[*] Starting the service analysis on {} ".format(Detect.Detect_Os())
                    app, host= Host_Linux.Detect_Linux()
        return app, hostname

daemon = Pyro4.Daemon(host='192.168.1.4' , port=4545)
ns = Pyro4.locateNS(host='192.168.1.4' , port=9898)

uri = daemon.register(execution)
ns.register('Apps2', uri)
daemon.requestLoop()
