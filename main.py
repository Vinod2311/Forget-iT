#!/bin/sh
from sense_hat import SenseHat
import time
import distance as dist
import blynk

while True:
    exec(open("distance.py").read())
    exec(open("blynk.py").read())
