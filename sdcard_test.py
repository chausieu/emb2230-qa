#!/usr/bin/env python
# coding=utf8


import time
import serial
import os
import socket
import commands
#import pexpect
import sys

usb_flag = -1

#usb
def usb():
	global usb_flag

	status, output = commands.getstatusoutput('ls /dev/mmcblk3p1')
	nPos = output.find('/dev/mmcblk3p1')

	print nPos
	if nPos == 0:
                status, output = commands.getstatusoutput('hdparm -T /dev/mmcblk3p1')
                print output
                                                 
                new_str,speed = output.split('=')
                str_speed = speed.split('MB/sec')
                            
                usb_flag = 0       
                return str_speed[0]		
	else:
                usb_flag = 1
                return 0.0
  	
#main	
if __name__ == '__main__':

	speed = usb()
	print speed

        if usb_flag == 0:
		if float(speed) > 200:
                	print "sdcard      test function success"
			sys.exit(0)
		else:
			print "sdcard      test function failure"
			sys.exit(1)
        else:
                print "usb      test function failure"
		sys.exit(1)
		
	print "------------------------- "

