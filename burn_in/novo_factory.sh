#!/bin/bash

/home/root/novo_test_20170307/burn_in/burn-in_gpio.py
res=`echo $?`   # get return result

if [ $res = "1" ]; then  
	echo "run burn-in"
	/home/root/novo_test_20170307/burn_in/burn-in_test.py &
else
	echo "run qt app"
	export QT_QPA_EGLFS_DISABLE_INPUT=1
	export QT_QPA_EGLFS_HIDECURSOR=1
	export TSLIB_TSDEVICE=/dev/input/event0
	export TSLIB_CALIBFILE=/etc/pointercal
	export TSLIB_CONFFILE=/etc/ts.conf
	export QT_QPA_GENERIC_PLUGINS=tslib:/dev/input/event0

	echo 32 > /sys/class/graphics/fb0/bits_per_pixel
	/home/root/novoqa -platform eglfs -plugin tslib & 
fi  
