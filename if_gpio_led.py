import subprocess
import importlib
import led

import traceback
import sys

pin = '23'
gpio_str = 'gpio wfi '+pin+ ' both'

l = led.LED()
l.use(0) # green
l.use(1) # red
l.off(0)
l.off(1)
l_status = False

def get_gpio():
  p = subprocess.call(gpio_str, stdout=subprocess.PIPE, shell=True)
  return p.stdout.readline().strip()


def wait():
  global l_status, l
  while True:
    try:
      print "start"
      p = subprocess.call(gpio_str, shell=True)
      print "end"
#      reader = importlib.import_module("read")
#      reader.read()
      if l_status:
        l.off(0)
        l.off(1)
        l_status = False
        print "off"
      else:
        l.on(0)
        l.on(1)
        l_status = True
        print "on"
    except:
      info=sys.exc_info()
      print "Unexpected error:"+ traceback.format_exc(info[0])
      print traceback.format_exc(info[1])
      print traceback.format_exc(info[2])

if __name__ == '__main__':
  print wait()