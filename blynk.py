#!/bin/sh
import BlynkLib
from sense_hat import SenseHat
import RPi.GPIO as GPIO
import time
import distance
import logging
from dotenv import dotenv_values


#Setup pir sensor for input data on GPIO pin 7
GPIO.setmode(GPIO.BCM)
GPIO.setup(7,GPIO.IN)

#Initialise SenseHAT
sense = SenseHat()

#Initialize global variables
bluetooth_proximity = 0
pir_proximity = 0

#Load configuration values from .env file
config = dotenv_values(".env")
#Initialize Blynk
blynk = BlynkLib.Blynk(config['BLYNK_AUTH_TOKEN'])
#Configure Logging
logging.basicConfig(level=logging.INFO)



#Detect proximity using ble beacon and update blynk app and senseHAT
@blynk.on("Read ble")
def bluetooth_sensor():
  strength = [0,0,0,0,0]
  global bluetooth_proximity
  distance.distance_calculated(strength)
  average_strength= sum(strength)/len(strength) 
  if average_strength > -50:
    bluetooth_proximity = 1
  elif average_strength < -50:
    bluetooth_proximity = 0
  print("ble strength: ",strength, " ble detection ", bluetooth_proximity)
  
  if bluetooth_proximity==1:
      blynk.virtual_write(0,1)
  elif bluetooth_proximity==0:  
      blynk.virtual_write(0,0)


#Detect proximity based on PIR sensor and update Blynk app
@blynk.on("Read pir")
def pir_sensor():
  global pir_proximity 
  if GPIO.input(7):
      blynk.virtual_write(1,1)
      pir_proximity = 1
      print("PIR:detected")
  else:
      blynk.virtual_write(1,0)
      pir_proximity = 0
      print("PIR:not detected")


#Calculate whether it is safe to leave
@blynk.on("Safe to leave")
def safe_to_leave():
  if bluetooth_proximity==1 and pir_proximity==1:
    blynk.virtual_write(2,1)
    sense.clear(0,255,0)
  else:
    blynk.virtual_write(2,0)
    sense.clear(255,0,0)


#Infinite loop to run Blynk
while True:
    bluetooth_sensor()
    pir_sensor()
    safe_to_leave()
    blynk.run()
    time.sleep(1)
