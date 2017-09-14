#!/usr/bin/python
import random

a=0 
b=1232
p=0.8
cont=0.0
a=0

for a in range(a,b):
 u=random.random()
 if(u<(1-p)):
   cont=cont+0
 else:
   cont=cont+1
 a=a+1


print float(cont/b)
