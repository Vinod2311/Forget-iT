#!/bin/sh
from ble_scanner import ScanUtility
import bluetooth._bluetooth as bluez
from sense_hat import SenseHat
import time

#start time
start_time = time.time()

#Set bluetooth device. Default 0.
dev_id = 0
strength = 0

#initialise SenseHAT
sense = SenseHat()
#sense.clear()

try:
	sock = bluez.hci_open_dev(dev_id)
	#print ("\n *** Looking for BLE Beacons ***\n")
	#print ("\n *** CTRL-C to Cancel ***\n")
except:
	print ("Error accessing bluetooth")

ScanUtility.hci_enable_le_scan(sock)
#Scans for iBeacons
try:
	#while True:
		returnedList = ScanUtility.parse_events(sock, 100)
		for item in returnedList:
			strength = item['rssi']
			
		current_time = time.time()
		#def distance(value):
		if strength > -50:
			sense.clear(0,255,0)
		elif strength < -60:
			sense.clear(255,0,0)
		print(strength, " ",current_time - start_time)
		
except KeyboardInterrupt:
    pass
