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
		rtc_flag = 0
	else:
		rtc_flag = 1

#main	
if __name__ == '__main__':

	rtc()
		
        if rtc_flag == 0:
		print "rtc      test function success"
		sys.exit(0)
        else:
                print "rtc      test function failure"
		sys.exit(1)
		
	print "------------------------- "

