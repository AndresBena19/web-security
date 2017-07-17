#!/usr/bin/python

import sys

caracteres = []

for caracter in sys.argv[1:]:
 caracteres.append(int(caracter, 0))

con = 0x00
test = '"'

print "[*] generando el test de caracteres"

while con <=0xFF:
	if con not in caracteres:
	 test +="\\x%02x" %con
	con += 1
test +='"'

print "[*]  Generacion completada"
print test  + "\n"
