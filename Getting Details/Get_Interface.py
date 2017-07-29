#!/usr/bin/python


import netifaces

def Interface():
    inter = netifaces.interfaces()
    return inter

def Gateway():
    Gatewayd = {}
    Gayw = netifaces.gateways()
    for p in Gayw:
        try:
            GT = Gayw[p][netifaces.AF_INET]
            GP, iface = GT[0], GT[1]
            GL =[GP, iface]
            Gatewayd[p]=GL
        except:
            pass
    return  Gatewayd

if __name__=="__main__":

 I = Interface()
 G = Gateway()
 print "The interfaces are:" 
 print(I) 
 print "The networks are:"
 print(G)

