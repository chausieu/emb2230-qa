#!/bin/sh

/etc/init.d/ntpd stop
/usr/sbin/ntpdate 192.168.1.10
/etc/init.d/ntpd start

date +%F > /home/root/novo_test_20170307/config/previous-time.conf

