#!/usr/bin/python

from FifoClass import Cola

q=Cola()


print q.es_vacia()

q.encolar(1)
q.encolar(2)

print q.es_vacia()
