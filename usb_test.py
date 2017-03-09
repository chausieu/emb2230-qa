#!/usr/bin/env python
# coding=utf8


import time
import serial
import os
import socket
import commands
#import pexpect
import sys

usb_flag = 0

#usb
def usb():
	global usb_flag

	status, output = commands.getstatusoutput('ls /dev/sda1')
	nPos = output.find('/dev/sda1')

	print nPos
	if nPos == 0:
                status, output = commands.getstatusoutput('hdparm -T /dev/sda1')
                print output
                                                 
                new_str,speed = output.split('=')
                str_speed = speed.split('MB/sec')
                            
                usb_flag = 1       
                return str_speed[0]		
	else:
                usb_flag = 0                     
                return 0.0
  	
#main	
if __name__ == '__main__':

	print "\n"
	print "\n"
	print "NOVO Test"
	print "\n"
	print "\n"

	speed = usb()
	print speed
		
	#sys.exit(1)

	os.system(" clear ")
	print "\n"
	
	print "------Test Results------- "

        if usb_flag == 1:
		if float(speed) > 200:
                	print "usb      test function success"
			sys.exit(0)
		else:
			print "usb      test function failure"
			sys.exit(1)
        else:
                print "usb      test function failure"
		sys.exit(1)
		
	print "------------------------- "

