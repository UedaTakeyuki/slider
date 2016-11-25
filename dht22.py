# coding:utf-8
# Copy Right Atelier Grenouille  © 2015 -
#
# require: 'lol_dht' https://github.com/technion/lol_dht22
# return:  {"temp": , "humidity":}

#import subprocess
import os
import sys
#import commands
#import subprocess
import subprocess32 as subprocess
import re
import slider_utils as slider

def dht22(gpio):
  try:
    #p = subprocess.Popen(["/home/pi/SCRIPT/vendor/lol_dht22/loldht", "29",  "|grep", "Hum"], 
    #                     stdin=subprocess.PIPE,
    #                     stdout=subprocess.PIPE,
    #                     stderr=subprocess.PIPE,
    #                     shell=False)
    #return p.stdout.readline()
    #usbrh_result = p.stdout.readline().split()
    #result = {"temp":float(usbrh_result[0]), "humidity":float(usbrh_result[1])}
    #return result

#    result = commands.getoutput("/home/pi/install/lol_dht22/loldht " + str(29) + " |grep Hum")
#    p = subprocess.Popen(os.path.abspath(os.path.dirname(__file__))+"/vendor/lol_dht22/loldht " + str(gpio) + " |grep Hum", stdout=subprocess.PIPE, shell=True)
    p = subprocess.Popen(os.path.abspath(os.path.dirname(__file__))+"/vendor/lol_dht22/loldht " + str(gpio) + " |grep Hum", stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    std_out, std_err = p.communicate(None, timeout=10)
    result = std_out.strip()

    # read result
    match = re.match(r'Humidity = (.*) % Temperature = (.*) \*C',result)
    temp = float(match.group(2))
    humidity =float(match.group(1))

    # drop bad value.
    if temp < -1000  or temp > 1000:
        temp = None
    if humidity < -1000 or humidity > 1000:
        humidity = None
    result = {"temp":temp, "humidity":humidity}
#    result = {"temp":float(match.group(2)), "humidity":float(match.group(1))}
    return result
  except IOError:
    slider.io_error_report()
  except:
    slider.unknown_error_report()

# http://d.hatena.ne.jp/Rion778/20121203/1354546179
def HumidityDeficit(t,rh): # t: 温度, rh: 相対湿度
    ret = AbsoluteHumidity(t, 100) - AbsoluteHumidity(t, rh)
#    print "HD = " + str(ret)
    return ret; 

# http://d.hatena.ne.jp/Rion778/20121203/1354461231
def AbsoluteHumidity(t, rh):
    ret = 2.166740 * 100 * rh * tetens(t)/(100 * (t + 273.15))
#    print "AH = " + str(ret)
    return ret


#  飽和水蒸気圧
#  function GofGra(t){};
# http://d.hatena.ne.jp/Rion778/20121126/1353861179
def tetens(t):
    ret = 6.11 * 10 ** (7.5*t/(t + 237.3))
#    print "tetens = " + str(ret)
    return ret

def read():
  result = dht22(29)
  if result is not None:
    result["humiditydeficit"] = ('%.1f' % HumidityDeficit(result["temp"],result["humidity"]))
    return result

if __name__ == '__main__':
    print dht22(29)

