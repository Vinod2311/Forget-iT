#!/bin/sh
from gpiozero import MotionSensor
import RPi.GPIO as GPIO


GPIO.setmode(GPIO.BCM)
GPIO.setup(7,GPIO.IN)

def pir_calculated(pir):
	try:
		if GPIO.input(7):
			pir = 1
		else:
			pir = 0
		print(pir)

	except KeyboardInterrupt:
		pass
	return pir
