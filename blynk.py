#!/bin/sh
import BlynkLib
from sense_hat import SenseHat
import time

import blynk_config as conf

BLYNK_AUTH = conf.BLYNK_AUTH_TOKEN

# initialize Blynk
blynk = BlynkLib.Blynk(BLYNK_AUTH)

#initialise SenseHAT
sense = SenseHat()
sense.clear()

# register handler for virtual pin V1 write event
@blynk.on("V0")
def v3_write_handler(value):
    buttonValue=value[0]
    print(f'Current button value: {buttonValue}')
    if buttonValue=="1":
        sense.show_message( "Stay", text_colour=[255,0,0])
    else:
        sense.clear()

#def distance(value):

#tmr_start_time = time.time()
# infinite loop that waits for event
while True:
    exec(open("distance.py").read())
    blynk.run()
    time.sleep(1)
