#!/usr/bin/python

import sys
try:
  import nmap
except:
  sys.exit("[!] Install the nmap library: pip install python-nmap")

scanner = nmap.PortScanner()
Result = scanner.scan('192.168.248.1', '21')

print(Result.csv())
