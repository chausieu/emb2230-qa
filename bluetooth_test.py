#!/usr/bin/env python
# coding=utf8


import time
import serial
import os
import socket
import commands
#import pexpect
import sys

bluetooth_flag = 0


#bluetooth
def bluetooth():
	global bluetooth_flag
	ser = serial.Serial('/dev/ttymxc3', 115200, timeout=1)
	ser.write("$$$")
	ser.write("\r\n")

	data = ser.read(10)
        print("read data: " + data)

	ser.write("+")
	ser.write("\r\n")

	#time.sleep(0.5)
	data = ser.read(10)
	print("read data: " + data)	

	if data.find("ECHO") >= 0:
		bluetooth_flag = 0
	else:
		bluetooth_flag = 1

#main	
if __name__ == '__main__':

	bluetooth()


        if bluetooth_flag == 0:
                print "bluetooth      test function success"
		sys.exit(0)
        else:
                print "bluetooth      test function failure"
		sys.exit(1)
	
		
	print "------------------------- "

