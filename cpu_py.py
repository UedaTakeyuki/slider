# -*- coding: utf-8 -*-
# 
# © Takeyuki UEDA 2017 - 

import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(__file__))+"/vendor")
import re
import cpuinfo

def remove_unit(val_unit_str):
  match = re.match('([0-9,.]*).*', val_unit_str)
  return match.group(1)

def read():
  return {'cpu_temp': remove_unit(cpuinfo.temp())}

if __name__ == '__main__':
  value = read()
  if value is not None:
    print value
  else:
    print "None"
