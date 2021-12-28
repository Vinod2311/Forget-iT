#!/bin/sh
import BlynkLib
from sense_hat import SenseHat
from gpiozero import MotionSensor
import RPi.GPIO as GPIO
import time
import distance
import logging
import config
#from dotenv import dotenv_values
import datetime
#import pir

#new_bluetooth_proximity = distance.bluetooth_proximity
#new_pir = pir_sensor.pir

GPIO.setmode(GPIO.BCM)
GPIO.setup(7,GPIO.IN)
BLYNK_AUTH_TOKEN = config.BLYNK_AUTH_TOKEN

#load MQTT configuration values from .env file
#config = dotenv_values(".env")
  # initialize Blynk
#blynk = BlynkLib.Blynk(config['BLYNK_AUTH_TOKEN'])
  #configure Logging
logging.basicConfig(level=logging.INFO)
# initialize Blynk

blynk = BlynkLib.Blynk(BLYNK_AUTH_TOKEN)

#initialise SenseHAT
sense = SenseHat()
#sense.clear()


@blynk.on("Read ble")
def bluetooth_sensor():
  strength = [0,0,0,0,0]
  bluetooth_proximity=0
  distance.distance_calculated(strength)
  average_strength= sum(strength)/len(strength)
  #print("average strength: ",average_strength)
  
  if average_strength > -50:
    bluetooth_proximity = 1
  elif average_strength < -50:
    bluetooth_proximity = 0
  #print("ble blynk script: ",strength, " ", bluetooth_proximity)
  #print("current script: ",strength," " ,bluetooth_proximity)
  if bluetooth_proximity==1:
      sense.clear(0,255,0)
      blynk.virtual_write(0,1)
      #print(bluetooth_proximity)
      time = datetime.datetime.now().strftime("%H:%M:%S")
      blynk.log_event("ble", f"Bluetooth proximity detected @: {time}")
  elif bluetooth_proximity==0: 
      #print(bluetooth_proximity,"no") 
      sense.clear(255,0,0)
      blynk.virtual_write(0,0)

@blynk.on("Read pir")
def pir_sensor(): 
  if GPIO.input(7):
      blynk.virtual_write(1,1)
      print("detected")
      time = datetime.datetime.now().strftime("%H:%M:%S")
      blynk.log_event("pir", "PIR proximity detected @: {time}")
      blynk.log_event("pir")
  else:
      blynk.virtual_write(1,0)
      print(GPIO.input(7),"not detected")

#bluetooth_sensor()

# infinite loop 
while True:
    
    #exec(open("distance.py").read())
    #exec(open("pir_sensor.py").read())
    bluetooth_sensor()
    pir_sensor()
    #print("stupid")
    blynk.run()
    time.sleep(1)
