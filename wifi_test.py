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
	os.system("insmod config/unifi_sdio.ko")
	os.system("sleep 5")
	
	status, output = commands.getstatusoutput('ifconfig -a ')
	if output.find("wlan0") > 0:
		wifi_flag = 0
	else:
        	wifi_flag = 1
		return 0.0

	os.system("ifconfig wlan0 up")
	os.system("ifconfig eth0 down")
	status, output = commands.getstatusoutput("wpa_supplicant -Dwext -iwlan0 -c config/wpa_supplicant.conf -B")
	os.system("sleep 5")
	status, output = commands.getstatusoutput("udhcpc -i wlan0")
	os.system("sleep 5")

	#iperf
	status, output = commands.getstatusoutput('iperf -c 192.168.0.166')
	str = output.split("\n")
	
	if len(str) < 2:
		wifi_flag = 1
		return 0.0
	
	new_str,speed = str[len(str) - 1].split('MBytes')
	str_speed = speed.split('Mbits/sec')
	wifi_flag = 0
	return str_speed[0]	

	
#main	
if __name__ == '__main__':

	speed = wifi()

        os.system("ifconfig wlan0 down")                                   
        #os.system("killall  unifi_helper") 
	#os.system("sleep 5")
                                
        #os.system("rmmod unifi_sdio")  
	#os.system("sleep 5")

	#sys.exit(1)

	print speed	

        if wifi_flag == 0:
		if float(speed) > 5:
                	print "wifi      test function success"
			sys.exit(0)
		else:
                	print "wifi      test function failure1"   
                	sys.exit(1) 			
        else:
                print "wifi      test function failure"
		sys.exit(1)
		
	print "------------------------- "

