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
 cont= a +(math.log1p(1.0-u)/math.log1p(p))
 a=a+1


print float(cont/b)
