from gpiozero import MotionSensor
from time import sleep

pir = MotionSensor(4)

while True:
  if pir.is_active:
    print("Active")
  else:
    print("Nope")
  sleep(3)
