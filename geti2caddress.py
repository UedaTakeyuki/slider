# coding:utf-8 Copy Right Atelier Ueda © 2016 -

import os
import subprocess

def addr():
  p = subprocess.Popen( os.path.dirname(os.path.abspath(__file__))+"/geti2caddress.sh ", stdout=subprocess.PIPE, shell=True)
  i2c_addr = p.stdout.readline().strip().decode('utf-8')
  return i2c_addr

if __name__ == '__main__':
  print (addr())
