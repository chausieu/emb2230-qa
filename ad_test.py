#!/usr/bin/env python
# coding=utf8


import time
import serial
import os
import socket
import commands
#import pexpect
import sys

ad_flag = 0

#ad
def ad():
	global ad_flag

	path = os.path.isfile("/sys/bus/i2c/drivers/ad7091r5/0-002f/iio:device0/in_voltage0_raw")
	if path == False:
		ad_flag = 0
		return

	
	pin = open("/sys/bus/i2c/drivers/ad7091r5/0-002f/iio:device0/in_voltage0_raw")
	value = pin.read()
	print "The ad value is:  %s,%d " %(str(value), int(value))
	pin.close()

	if int(value) > 1600 and int(value) < 1950:
		ad_flag = 1
	else:
		ad_flag = 0
		return

        pin = open("/sys/bus/i2c/drivers/ad7091r5/0-002f/iio:device0/in_voltage1_raw")
        value = pin.read()
        print "The ad value is:  %s,%d " %(str(value), int(value))
        pin.close()

        if int(value) > 1200 and int(value) < 1450:
                ad_flag = 1
        else:
                ad_flag = 0
                return

        pin = open("/sys/bus/i2c/drivers/ad7091r5/0-002f/iio:device0/in_voltage2_raw")
        value = pin.read()
        print "The ad value is:  %s,%d " %(str(value), int(value))
        pin.close()

        if int(value) > 0 and int(value) < 200:
                ad_flag = 1
        else:
                ad_flag = 0
                return

	
#main	
if __name__ == '__main__':

	print "\n"
	print "\n"
	print "NOVO Test"
	print "\n"
	print "\n"

	ad()
	#sys.exit(1)

	os.system(" clear ")
	print "\n"
	
	print "------Test Results------- "

        if ad_flag == 1:
                print "ad      test function success"
		sys.exit(0)
        else:
                print "ad      test function failure"
		sys.exit(1)
		
	print "------------------------- "

