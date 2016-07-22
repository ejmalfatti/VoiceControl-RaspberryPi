#!/usr/bin/python
# -*- coding: utf-8-*-
import os
import time

i=0

while i != 1 :
	infile = open('capture.txt', 'r')

	for line in infile:
		if line.find("encender luz") != -1 :
			print "Encendiendo la luz"
			#os.system("echo 0 > /sys/class/gpio/gpio17/value")
			os.system("true > capture.txt")
			#os.system("festival -b '(SayText "Green led off")'")
		if line.find("apagar luz") != -1 :
			print "Apagando la luz"
			#os.system("echo 1 > /sys/class/gpio/gpio17/value")
			os.system("true > capture.txt")
			#os.system("festival -b '(SayText "Green led ON")'")
		if line.find("tengo frío") != -1 :
			print "Tengo frío, que venga el calor"
			#os.system("echo 0 > /sys/class/gpio/gpio2/value")
			os.system("true > capture.txt")
			#os.system("festival -b '(SayText "Red led Off")'")
		if line.find("tengo calor") != -1 :
			print "Tengo calor, venga el fresco"
			#os.system("echo 1 > /sys/class/gpio/gpio2/value")
			os.system("true > capture.txt")
			#os.system("festival -b '(SayText "Red led ON")'")
		if line.find("EXIT") != -1 :
			os.system("sudo pkill -9 pocketsphinx")
			os.system("true > capture.txt")
			#os.system("festival -b '(SayText "Goodbye!")'")
			i=1

infile.close()
time.sleep(2)
