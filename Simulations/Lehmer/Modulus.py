#!/usr/bin/python

import fractions 

def fun(a):
  m=(2**31)-1
  q=m/a
  r=m%a
  if(r<q):
    print "is a modulus compatible:", r, "<", q
  else:
    print "is not a modulus comaptible:", r,">", q


if __name__ == "__main__":
  fun(1343714438)
