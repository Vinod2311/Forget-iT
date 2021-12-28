#!/bin/sh
from ble_scanner import ScanUtility
import bluetooth._bluetooth as bluez
from sense_hat import SenseHat
import time

#start time
start_time = time.time()

#Set bluetooth device. Default 0.
dev_id = 0
#strength = [0,0,0,0,0]
#bluetooth_proximity = 0

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

#def average_strength(input):
#	return sum(input)/len(input)
	

#Scans for iBeacons
def distance_calculated(strength):
	try:
		for i in range(len(strength)):
			returnedList = ScanUtility.parse_events(sock, 100)
			for item in returnedList:
				strength[i] = item['rssi']
		
		#current_time = time.time()
		#average_strength= sum(strength)/len(strength)
		#print("average strength: ",average_strength)
		#print("ble before update",bluetooth_proximity_input)
		#if average_strength > -50:
		#	sense.clear(0,255,0)
	#		bluetooth_proximity_input = 1
		#elif average_strength < -50:
		#	sense.clear(255,0,0)
		#	bluetooth_proximity_input = 0
		#print("ble after update",bluetooth_proximity_input)
		#print("old script: ",strength," ",bluetooth_proximity_input)
			
	except KeyboardInterrupt:
		pass
