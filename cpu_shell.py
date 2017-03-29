# -*- coding: utf-8 -*-
# 
# © Takeyuki UEDA 2017 - 


import subprocess
import re

def remove_unit(val_unit_str):
  match = re.match('([0-9,.]*).*', val_unit_str)
  return match.group(1)

def read():
  p = subprocess.Popen("vcgencmd measure_temp", stdout=subprocess.PIPE, shell=True)
  value = p.stdout.readline().strip().split('=')[1]
  return {'cpu_temp': remove_unit(value)}

if __name__ == '__main__':
  value = read()
  if value is not None:
    print value
  else:
    print "None"
