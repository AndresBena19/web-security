# Detection application's #

El siguiente script tiene como principal objetivo  detectar que aplicaciones y que version de la misma, se encuentran instaladas, ademas hace uso del modulo python-nmap, que le permite descubrir que servicios se encuentran activos  y cada una de sus interfaces 

## Requirements ##

+ python2.14
	* python-nmap library
	* netifaces library
	* unicode library
	* threading library
	* winreg (in the case of windows)
	* errno library
	* subprocess library (Default)
	* socket library (Default)
	* Platform library (Default)


## issues ##



```
PortScannerError: 'nmap program was not found in path. PATH is : C:\\Python27;C:\\Python27\\S
cripts;C:\\WINDOWS\\System32\\wbem;C:\\WINDOWS\\system32;C:\\WINDOWS;C:\\WINDOWS\\system32\\
WBEM;C:\\Users\\andresfelipe\\AppData\\Local\\GitHubDesktop\\bin;C:\\Python27

```

```
PortScannerError 'nmap' don't have the attribure PortScanner

```

## Solutions  ##


+ Windows 
	* you must install nmap project 
	+ You must establish
		* C:\Python27 (we need for the execution) 
		* C:\Python27\Scripts (We need pip to install the libraries
		* C:\WINDOWS\System32\wbem  (Unnecesary now, but it will help in the future, it's something fail when the script 									analize the registry
		* C:\Program Files (x86)\Nmap , (the method PortScanner don't work good on windows, this fix that)
		 
 




## Run Process  ##

Firt we need to run the setup.py , this gonna install all the libraries necesary for the correct execution of the script

```
Python setup.py
```
