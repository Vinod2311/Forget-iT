#!/bin/sh
from ble_scanner import ScanUtility
import bluetooth._bluetooth as bluez


#Set bluetooth device and enable scanning
dev_id = 0
try:
	sock = bluez.hci_open_dev(dev_id)
except:
	print ("Error accessing bluetooth")
ScanUtility.hci_enable_le_scan(sock)



#Scans for iBeacons
def distance_calculated(strength):
	try:
		for i in range(len(strength)):
			returnedList = ScanUtility.parse_events(sock, 100)
			for item in returnedList:
				strength[i] = item['rssi']
			
	except KeyboardInterrupt:
		pass
