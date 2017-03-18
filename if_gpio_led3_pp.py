# coding:utf-8 Copy Right Atelier Grenouille © 2015 -
#import subprocess
import importlib
import led
import RPi.GPIO as GPIO

import traceback
import sys
import getrpimodel

# RPi 3 は LED1(赤LED)を操作できない
pi3 = True if getrpimodel.model() == "3 Model B" else False

l = led.LED()
l.use(0) # green
pi3 or l.use(1) # red
l.off(0)
pi3 or l.off(1)
l_status = False

# GPIO の設定
GPIO.setmode(GPIO.BCM)

#def get_gpio():
#  p = subprocess.call(gpio_str, stdout=subprocess.PIPE, shell=True)
#  return p.stdout.readline().strip()


def wait(pin):
  global l
  GPIO.setup(int(pin), GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
  while True:
    try:
      print "waiting..."
      GPIO.wait_for_edge(int(pin), GPIO.RISING)
      #gpio_str = 'gpio wfi '+str(pin)+ ' rising'
      #p = subprocess.call(gpio_str, shell=True)
      l.on(0)
      pi3 or l.on(1)
      print "on"

      GPIO.wait_for_edge(int(pin), GPIO.FALLING)
      #gpio_str = 'gpio wfi '+str(pin)+ ' falling'
      #p = subprocess.call(gpio_str, shell=True)
      l.off(0)
      pi3 or l.off(1)
      print "off"

    except:
      info=sys.exc_info()
      print "Unexpected error:"+ traceback.format_exc(info[0])
      print traceback.format_exc(info[1])
      print traceback.format_exc(info[2])

if __name__ == '__main__':
  pin = 23
  if (len(sys.argv) == 2):
    pin = int(sys.argv[1])
  print wait(pin)
