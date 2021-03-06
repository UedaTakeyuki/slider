# coding:utf-8 Copy Right Atelier Grenouille © 2015 -
import subprocess
import importlib
import led

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

def get_gpio():
  p = subprocess.call(gpio_str, stdout=subprocess.PIPE, shell=True)
  return p.stdout.readline().strip()


def wait(pin):
  global l_status, l
  while True:
    try:
      print "start"
      gpio_str = 'gpio wfi '+str(pin)+ ' rising'
      p = subprocess.call(gpio_str, shell=True)
      print "end"
      if l_status:
        l.off(0)
        pi3 or l.off(1)
        l_status = False
        print "off"
      else:
        l.on(0)
        pi3 or l.on(1)
        l_status = True
        print "on"
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
