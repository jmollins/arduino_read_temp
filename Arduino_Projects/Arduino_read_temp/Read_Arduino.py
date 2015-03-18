#!/usr/bin/env python
# -*- coding: utf-8 -*-
#

import serial
import re
import requests
import ConfigParser

def sendToThingSpeak(temperature, api_key):
	Parameters={"key":api_key, "field1":temperature.group(1)}
	response=requests.post("https://api.thingspeak.com/update", params=Parameters)
	return (response)


print "Starting ..."
config = ConfigParser.ConfigParser()
config.read('config.cfg')
api_key = config.get('default','api_key')

#Search pattern for the temperature value	
dataForm = r'Temperature: (\d+\.\d*)'
repeat = True

#set up the USB port
print "Setting up serial ..."
ser = serial.Serial('/dev/ttyUSB0', 9600, timeout=None)

while(repeat):
#read in the temperature from the Arduino	
	dataLine=ser.readline()
	
	if dataLine: #if the reading was successful
		temperature=re.search(dataForm,dataLine) #extract the temperature from the reading
		if temperature:
			print temperature.group(1) 
			repeat=False
			response = sendToThingSpeak(temperature, api_key)
			print response
serial.close()
			

			
		
	
	

 
