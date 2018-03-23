#!/usr/bin/python

import fractions

def fun(a):

 cont=0
 Y=0
 m=32749
 i=1
 x=a

 while(x!=1):
  if(((m%x)<(m/x)) and fractions.gcd(i,m-1)==1):
   w=(a**i)%m
   dictq.insert(cont,int(w))
   cont=cont+1
  q=m/a
  r=m%a

  t=a*(x%q)-r*(x/q)
  if (t>0):
     Y=0
  else:
     Y=1
  x=t+m*Y
  i=i+1
 return cont


if __name__ == "__main__":
  dictq=[]
  b=fun(3)

  print ("The full periods multipliers modulus compatible:")
  print (dictq)


  print "The number of items:",b
