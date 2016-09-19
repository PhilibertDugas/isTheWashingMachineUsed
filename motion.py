#!/usr/bin/python3

from gpiozero import MotionSensor
from time import sleep, strftime
import sys

pir = MotionSensor(4)

while True:
  current_time = strftime("%Y-%m-%d %H:%M:%S")
  if pir.is_active:
    sys.stdout.write("[%s] Active\n" % current_time)
  else:
    sys.stdout.write("[%s] Inactive\n" % current_time)
  sys.stdout.flush()
  sleep(30)
