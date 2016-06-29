# http://eleparts.co.kr/data/design/product_file/SENSOR/gas/MH-Z19_CO2%20Manual%20V2.pdf
import serial
import time
import subprocess

stop_getty = 'sudo systemctl stop serial-getty@ttyAMA0.service'
start_getty = 'sudo systemctl start serial-getty@ttyAMA0.service'


def mh_z19():
  ser = serial.Serial('/dev/ttyAMA0',
                      baudrate=9600,
                      bytesize=serial.EIGHTBITS,
                      parity=serial.PARITY_NONE,
                      stopbits=serial.STOPBITS_ONE,
                      timeout=1.0)
  while 1:
    result=ser.write("\xff\x01\x86\x00\x00\x00\x00\x00\x79")
    s=ser.read(9)
    if s[0] == "\xff" and s[1] == "\x86":
      return {'co2': ord(s[2])*256 + ord(s[3])}
    break

def read():
  p = subprocess.call(stop_getty, stdout=subprocess.PIPE, shell=True)
  result = mh_z19()
  p = subprocess.call(start_getty, stdout=subprocess.PIPE, shell=True)
  return {'CO2': result["co2"]}

if __name__ == '__main__':
  value = mh_z19()
  print "co2=", value["co2"]
