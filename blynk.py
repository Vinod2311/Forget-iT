#!/bin/sh
import BlynkLib
from sense_hat import SenseHat
import time

import blynk

BLYNK_AUTH = $BLYNK_AUTH_TOKEN

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
        sense.clear(255,255,255)
    else:
        sense.clear()

#tmr_start_time = time.time()
# infinite loop that waits for event
while True:
    blynk.run()
    time.sleep(1)
