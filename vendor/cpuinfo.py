# -*- coding: utf-8 -*-
# refer http://www.elinux.org/RPI_vcgencmd_usage
# 
# © Takeyuki UEDA 2017 - 

import subprocess
# import re

def get_cpu_info(param_str):
  command_str = "vcgencmd " + param_str
  p = subprocess.Popen(command_str, stdout=subprocess.PIPE, shell=True)
#  match = re.match('([0-9,.]*).*', p.stdout.readline().strip().split('=')[1])
#  return match.group(1)
  return p.stdout.readline().strip().split('=')[1]

def temp():
  return get_cpu_info("measure_temp")

def clock_arm():
  return get_cpu_info("measure_clock arm")

def clock_core():
  return get_cpu_info("measure_clock core")

def clock_uart():
  return get_cpu_info("measure_clock uart")

def codec_enabled_H264():
  return get_cpu_info("codec_enabled H264")

def codec_enabled_MPG2():
  return get_cpu_info("codec_enabled MPG2")

def codec_enabled_WVC1():
  return get_cpu_info("codec_enabled WVC1")

def mem_usage_arm():
  return get_cpu_info("get_mem arm")

def mem_usage_gpu():
  return get_cpu_info("get_mem gpu")


if __name__ == '__main__':
  print "temp = {}".format(temp())
  print "clock frequency of arm = {}".format(clock_arm())
  print "clock frequency of core = {}".format(clock_core())
  print "clock frequency of uart = {}".format(clock_uart())
  print "codec enabled of H264 = {}".format(codec_enabled_H264())
  print "codec enabled of MPG2 = {}".format(codec_enabled_MPG2())
  print "codec enabled of WVC1 = {}".format(codec_enabled_WVC1())
  print "memory usage of arm = {}".format(mem_usage_arm())
  print "memory usage of gpu = {}".format(mem_usage_gpu())
