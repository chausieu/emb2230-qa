#!/usr/bin/env python
# coding=utf8


import time
import serial
import os
import socket
import commands
#import pexpect
import sys

gpio_flag = 0

#gpio__
def export_pins(pins):
        try:
                f = open("/sys/class/gpio/export","w")
                f.write(str(pins))
                f.close()
        except IOError:
                print "GPIO %s already Exists, so skipping export gpio" % (str(pins), )

def unexport_pins(pins):
        try:
                f = open("/sys/class/gpio/unexport","w")
                f.write(str(pins))
                f.close()
        except IOError:
                print "GPIO %s is not found, so skipping unexport gpio" % (str(pins), )


def setpindirection(pin_no, pin_direction):
	gpiopin = "gpio%s" % (str(pin_no))
        pin = open("/sys/class/gpio/"+gpiopin+"/direction","w")
        pin.write(pin_direction)
        pin.close()


def writepins(pin_no, pin_value):
        gpiopin = "gpio%s" % (str(pin_no))
        pin = open("/sys/class/gpio/"+gpiopin+"/value","w")
        if pin_value == 1:
                pin.write("1")
        else:
                pin.write("0")

	pin.close()

def readpins(pin_no):
        gpiopin = "gpio%s" % (str(pin_no), )
        pin = open("/sys/class/gpio/"+gpiopin+"/value","r")
        value = pin.read()
        print "The value on the PIN %s is : %s" % (str(pin_no), str(value))
        pin.close()
        return int(value)

		
#gpio
def gpio():
	global gpio_flag

	#p20_14 
	export_pins(114)
	setpindirection(114, "out")
	writepins(114, 1)
	unexport_pins(114)

	#p20_15
        export_pins(116)
        setpindirection(116, "in")
        value = readpins(116)
        print "116 The gpio value is: %d " %(int(value))
        unexport_pins(116)
        if value == 1:
                gpio_flag = 0
        else:
                gpio_flag = 1
                return	
		
#main	
if __name__ == '__main__':

	gpio()

        if gpio_flag == 0:
                print "gpio      test function success"
		sys.exit(0)
        else:
                print "gpio      test function failure"
		sys.exit(1)
		
	print "------------------------- "

