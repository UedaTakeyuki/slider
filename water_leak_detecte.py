import subprocess
import importlib
import led

import traceback
import sys
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)

GPIO.setup(36, GPIO.OUT)
GPIO.setup(38, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.output(36, GPIO.HIGH)

l = led.LED()
l.use(0) # green
l.use(1) # red

l.on(0)  # green on
l.off(1) # red off


def wait():
  while True:
    try:
      GPIO.wait_for_edge(38, GPIO.RISING)
      l.off(0) # greenn off
      l.on(1)  # red on
      print "send alart on"
      while True:
        if not GPIO.input(38):
          l.on(0)  # green on
          l.off(1) # red off
          print "send alart off"
          break;
        time.sleep(60)
    except:
      info=sys.exc_info()
      print "Unexpected error:"+ traceback.format_exc(info[0])
      print traceback.format_exc(info[1])
      print traceback.format_exc(info[2])

if __name__ == '__main__':
  print wait()