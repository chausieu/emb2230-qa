#!/usr/bin/env python
# coding=utf8


import time
import serial
import os
import socket
import commands
#import pexpect
import sys
import datetime

rtc_flag = 0

#rtc
def rtc():
	global rtc_flag
	str = datetime.datetime.now()  
	
	print str.year
	if str.year == 2017:
		rtc_flag = 1
	else:
		rtc_flag = 0

#main	
if __name__ == '__main__':

	print "\n"
	print "\n"
	print "NOVO Test"
	print "\n"
	print "\n"

	rtc()
		
	#sys.exit(1)

	os.system(" clear ")
	print "\n"
	
	print "------Test Results------- "

        if rtc_flag == 1:
		print "rtc      test function success"
		sys.exit(0)
        else:
                print "rtc      test function failure"
		sys.exit(1)
		
	print "------------------------- "

