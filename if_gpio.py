import subprocess
import importlib

pin = '23'
gpio_str = 'gpio wfi '+pin+ ' falling'

def get_gpio():
  p = subprocess.call(gpio_str, stdout=subprocess.PIPE, shell=True)
  return p.stdout.readline().strip()


def wait():
  while True:
    try:
      p = subprocess.call(gpio_str, shell=True)
      reader = importlib.import_module("read")
      reader.read()
    except:
    	pass

if __name__ == '__main__':
  print wait()