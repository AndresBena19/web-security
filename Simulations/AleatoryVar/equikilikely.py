#!/usr/bin/python
import random
import math

a=0 
b=1000


p=0.8
cont=0.0
a=0

for a in range(a,b):
 u=random.random()
 cont= a+(u*(b-a+1))
 a=a+1


print float(cont/b)
