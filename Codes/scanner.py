#!/bin/python

import sys # allows us to enter command line arguments, among other things
import socket
from datetime import datetime

#define our target
if len(sys.argv) == 2:
    	target = socket.gethostbyname(sys.argv[1]) # translate a host name to IPV4
else:
    	print("Invalid amount of arguments.")
    	print("Syntax python3 scanner.py <ip>")
    	#sys.exit()

#add a pretty banner
print("-" * 50)
print("Scanner target "+target)
print("Time started: "+str(datetime.now()))
print("-" * 50)

try:
    	for port in range(50,85):
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        	socket.setdefaulttimeout(1) # is a float
        	print("checking port {}".format(port))
       	 	result = s.connect_ex((target,port)) # returns error indicator
        	if result == 0:
            		print("Port {} is open".format(port))
            	s.close()

except KeyboardInterrupt:
    	print("\nExiting program")
    	sys.exit()

except socket.gaierror:
    	print("hostname could not be resolved")
    	sys.exit()

except socket.error:
    	print("couldn't connect to server")
    	sys.exit()