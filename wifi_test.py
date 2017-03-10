#!/usr/bin/env python
# coding=utf8


import time
import serial
import os
import socket
import commands
#import pexpect
import sys
#import iperf3

wifi_flag = 0

#wifi
def wifi():	
	status, output = commands.getstatusoutput('ifconfig -a ')
	if output.find("wlan0") > 0:
		wifi_flag = 0
	else:
        	wifi_flag = 1
		return 0.0

	os.system("ifconfig wlan0 up")
	os.system("ifconfig eth0 down")
	os.system("wpa_supplicant -Dwext -iwlan0 -c /home/root/novo_test_20170307/config/wpa_supplicant.conf -B")
	os.system("udhcpc -i wlan0")
	
#main	
if __name__ == '__main__':

	wifi()

        os.system("ifconfig wlan0 down")                                   
	os.system("ifconfig eth0 up")
	os.system("udhcpc -i eth0")
        

        if wifi_flag == 0:
                print "wifi      test function success"
		sys.exit(0)
					
        else:
                print "wifi      test function failure"
		sys.exit(1)
		
	print "------------------------- "

