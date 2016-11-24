# -*- coding: utf-8 -*-
#
# © Takeyuki UEDA 2016 -.

#import getpirevision
import re
import sys


usage = 'Usage: python {} [--s]'.format(__file__)

# model definition table from revision info.
# refer http://elinux.org/RPi_HardwareHistory
model_a          = ["0007","0008","0009",]
model_b          = ["0002","0004","0005","0006",]
model_b_beta     = ["Beta",]
model_b_ECN0001  = ["0003",]
model_cm         = ["0011","0011",]
model_a_plus     = ["0012","0015",]
model_b_plus     = ["0010","0013",]
model_2b         = ["a01040","a01041","a21041",]
model_2b_2837    = ["a22042",]
model_3b         = ["a02082", "a22082",]
model_zero       = ["900092","900093","920093",]

def revision():
  revision = "unknown"
  with open('/proc/cpuinfo', 'r') as f:
    for line in f:
      m = re.search('Revision.*: ([0123456789abcdef]*)', line)
      if m:
        revision = m.group(1)
        return revision

def model_strict():
#  rev = getpirevision.revision()
  rev = revision()
  if rev in model_a:
    return "A"
  elif rev in model_b:
    return "B"
  elif rev in model_b_beta:
    return "B (Beta)"
  elif rev in model_b_ECN0001:
    return "B (ECN0001)"
  elif rev in model_cm:
    return "Compute Module"
  elif rev in model_a_plus:
    return "A+"
  elif rev in model_b_plus:
    return "B+"
  elif rev in model_2b:
    return "2 Model B"
  elif rev in model_2b_2837:
    return "2 Model B (with BCM2837)"
  elif rev in model_3b:
    return "3 Model B"
  elif rev in model_zero:
    return "Zero"
  else:
    return None

def model():
#  rev = getpirevision.revision()
  rev = revision()
  if rev in model_a:
    return "A"
  elif rev in model_b + model_b_beta + model_b_ECN0001:
    return "B"
  elif rev in model_cm:
    return "Compute Module"
  elif rev in model_a_plus:
    return "A+"
  elif rev in model_b_plus:
    return "B+"
  elif rev in model_2b + model_2b_2837:
    return "2 Model B"
  elif rev in model_3b:
    return "3 Model B"
  elif rev in model_zero:
    return "Zero"
  else:
    return None

if __name__ == '__main__':
  if len(sys.argv) == 1:
    print (model())
  elif len(sys.argv) == 2:
    if sys.argv[1] == '--s':
      print (model_strict())
    else:
      print usage
  else:
    print usage