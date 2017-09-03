#!/usr/bin/python
import fractions 
def FullP(a):
  cont=0 
  m=2147483648
  i=1
  x=a
  while(x!=1):
   if(fractions.gcd(i , m-1)==1):
     w=(a**i)%m
     cont=cont+1
     print "i:", i
     print "full period multiplier relative to m:", w
     print "---------------------------------------"
   i=i+1
   x=(a*x)%m
  return cont
if __name__ == "__main__":

  a=FullP(7)
  print "El numero de full periods es:",a
