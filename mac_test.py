#!/usr/bin/env python
# coding=utf8


import time
import serial
import os
import socket
import commands
#import pexpect
import sys

mac_flag = 0

#usb
def mac():
	global mac_flag

	path = os.path.isfile("/sys/class/net/eth0/address")
	#print path

	if path == True:
		mac = open('/sys/class/net/eth0/address').readline()
		mac_fix = '10:07:23:6'

		#print mac_fix
		nPos = mac.find(mac_fix)

		if nPos == 0:
			mac_flag = 0 
		else:
			mac_flag = 1
	else:
		mac_flag = 1

	
#main	
if __name__ == '__main__':

	print "\n"
	print "\n"
	print "NOVO Test"
	print "\n"
	print "\n"

	mac()
	#sys.exit(1)

	os.system(" clear ")
	print "\n"
	
	print "------Test Results------- "

        if mac_flag == 0:
                print "mac      test function success"
		sys.exit(1)
        else:
                print "mac      test function failure"
		sys.exit(0)
		
	print "------------------------- "

