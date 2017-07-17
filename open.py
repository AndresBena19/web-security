#! /usr/bin/python

doc = open("/etc/passwd", "r")
    
for line in doc.readlines():
	 print line.strip()
 
doc.close()
