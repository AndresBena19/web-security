#!/usr/bin/python

import random


def  binomial(n,p):

 cont=0.0
 for a in range(0,n):
   u=random.random()
   if(u<(1-p)):
    cont=cont+0
   else:
    cont=cont+1
 return cont




if __name__ == "__main__":

   n=1000
   p=0.8
   cont=binomial(n,p)
   print float(cont/n)
