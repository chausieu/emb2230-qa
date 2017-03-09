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
	export_pins(154)
	setpindirection(154, "out")
	writepins(154, 1)
	unexport_pins(154)

	#p20_21
	export_pins(155)
	setpindirection(155, "out")
	writepins(155, 1)
	unexport_pins(155)

	#p20_5
        export_pins(106)
        setpindirection(106, "in")
	value = readpins(106)
	print "11The gpio value is: %d " %(int(value))
	unexport_pins(106)
	if value == 1:
		gpio_flag = 1
	else:
		gpio_flag = 0
		return

        #p20_22
        export_pins(156)
        setpindirection(156, "out")
        writepins(156, 1)
        unexport_pins(156)

        #p20_23
        export_pins(157)
        setpindirection(157, "out")
        writepins(157, 1)
        unexport_pins(157)

        #p20_15
        export_pins(103)
        setpindirection(103, "in")
        value = readpins(103)
        print "22The gpio value is: %d " %(int(value))
        unexport_pins(103)
        if value == 1:
                gpio_flag = 1
        else:
                gpio_flag = 0
                return	
		
#main	
if __name__ == '__main__':

	print "\n"
	print "\n"
	print "NOVO Test"
	print "\n"
	print "\n"

	gpio()
	#sys.exit(1)

	os.system(" clear ")
	print "\n"
    #print "\n"
	print "------Test Results------- "

        if gpio_flag == 1:
                print "gpio      test function success"
		sys.exit(0)
        else:
                print "gpio      test function failure"
		sys.exit(1)
		
	print "------------------------- "

