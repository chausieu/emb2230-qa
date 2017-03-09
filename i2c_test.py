#!/usr/bin/env python
# coding=utf8


import time
import serial
import os
import socket
import commands
#import pexpect
import sys

i2c_flag = 0

#i2c
def i2c():
        global i2c_flag
        status, output = commands.getstatusoutput('i2cdetect -y 0')
        #print output
        if output.find("Error") > 0:
                i2c_flag = 0
		return
        else:
                i2c_flag = 1


	os.system('i2cset -f -y 0 0x50 0x10 5')
	status, output = commands.getstatusoutput('i2cget  -y 0 0x50 0x10 ')
	print output
	if output.find("05") > 0:
		i2c_flag = 1
	else:
		i2c_flag = 0

	
#main	
if __name__ == '__main__':

	print "\n"
	print "\n"
	print "NOVO Test"
	print "\n"
	print "\n"

	i2c()
	#sys.exit(1)

	os.system(" clear ")
	print "\n"
	
	print "------Test Results------- "

        if i2c_flag == 1:
                print "i2c      test function success"
		sys.exit(0)
        else:
                print "i2c      test function failure"
		sys.exit(1)
		
	print "------------------------- "

