import Pyro4
if __name__ == '__main__':

    ns = Pyro4.locateNS(host='192.168.1.5' , port=9898)

    uri = ns.lookup('Apps')

    Host_Windows = Pyro4.Proxy(uri)

    #We instance a objetc from windows class
    Host= Host_Windows.exec_app()

    print Host
