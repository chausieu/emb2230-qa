#!/usr/bin/env python
# coding=utf8


import time
import serial
import os
import socket
import commands
#import pexpect
import sys

serial_flag = 0

#serial	
def serial_f():
	global serial_flag 
	ser = serial.Serial('/dev/ttymxc2', 115200, timeout=1)
	ser.write("0123456789")
	if ser.read(10) == "0123456789":
		serial_flag = 1
	else:
		serial_flag = 0
		return
		
        ser = serial.Serial('/dev/ttymxc4', 115200, timeout=1)
        ser.write("9876543210")
        if ser.read(10) == "9876543210":
                serial_flag = 1
        else:
                serial_flag = 0
                return

	
#main	
if __name__ == '__main__':

	print "\n"
	print "\n"
	print "NOVO Test"
	print "\n"
	print "\n"

	serial_f()
	#sys.exit(1)

	os.system(" clear ")
	print "\n"
	
	print "------Test Results------- "

        if serial_flag == 1:
                print "serial      test function success"
		sys.exit(0)
        else:
                print "serial      test function failure"
		sys.exit(1)
		
	print "------------------------- "

