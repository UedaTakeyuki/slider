# coding:utf-8 Copy Right Atelier Grenouille © 2015 -
#
import os
import subprocess
import importlib
import led

import traceback
import sys
import RPi.GPIO as GPIO
import time

import ConfigParser
import requests
import getserialnumber as gs
import getrpimodel

# RPi 3 は LED1(赤LED)を操作できない
pi3 = True if getrpimodel.model() == "3 Model B" else False

# 設定の取得
ini = ConfigParser.SafeConfigParser()
configfile = os.path.dirname(os.path.abspath(__file__))+'/gen_sender.ini' #センダーと同じ設定
ini.read(configfile) #繰り返し毎に設定を取得

# GPIO の設定
GPIO.setmode(GPIO.BOARD)

GPIO.setup(36, GPIO.OUT)
GPIO.setup(38, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.output(36, GPIO.HIGH)

# 基盤LED の設定
l = led.LED()
l.use(0) # green
pi3 or l.use(1) # red

if GPIO.input(38):
  l.off(0)  # green off
  pi3 or l.on(1) # red on
else:
  l.on(0)  # green on
  pi3 or l.off(1) # red off

def wait():
  while True:
    try:
      #GPIO.wait_for_edge(38, GPIO.RISING) # GPIO problem? mb both.
      if GPIO.input(38):
        l.off(0) # greenn off
        pi3 or l.on(1)  # red on
        payload = {'serial_id': gs.get_serialnumber(), 'name': "water", 'status': "on"}
        r = requests.post(ini.get("server", "url_base") + 'postalart.php', data=payload, timeout=10, cert=os.path.dirname(os.path.abspath(__file__))+'/slider.pem', verify=False)
        print "send alart on"

        while True:
          if not GPIO.input(38):
            return True
          time.sleep(30)
          #l.on(0)  # green on
          #l.off(1) # red off
          #payload = {'serial_id': gs.get_serialnumber(), 'name': "water", 'status': "off"}
          #r = requests.post(ini.get("server", "url_base") + 'postalart.php', data=payload, timeout=10, cert=os.path.dirname(os.path.abspath(__file__))+'/slider.pem', verify=False)
          #print "send alart off"
          #break;
        #time.sleep(60)
    except:
      info=sys.exc_info()
      print "Unexpected error:"+ traceback.format_exc(info[0])
      print traceback.format_exc(info[1])
      print traceback.format_exc(info[2])
    time.sleep(1)

def fork():
  pid = os.fork()
  if pid > 0:
    f = open('/var/run/water_leak_detecte.pid','w')
    f.write(str(pid)+"\n")
    f.close()
    sys.exit()

  if pid == 0:
    wait()

if __name__ == '__main__':
  print fork()