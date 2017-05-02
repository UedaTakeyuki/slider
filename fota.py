# coding:utf-8 Copy Right Atelier Grenouille © 2015 -
import os
import requests
import json
import subprocess
import logging
import sys 
import ConfigParser

import getserialnumber as gs
import slider_utils as slider

#定数および設定値
reboot = "sudo reboot"
#logfile = "/home/pi/LOG/fota.log"
configfile = '/home/pi/SCRIPT/slider/config.ini'
#logging.basicConfig(format='%(asctime)s %(filename)s %(lineno)d %(levelname)s %(message)s',filename=logfile,level=logging.DEBUG)

# 設定の取得
ini = ConfigParser.SafeConfigParser()
ini.read(configfile) #繰り返し毎に設定を取得
server_url_base = ini.get("server", "url_base")

#設定値に依存する定数
fota_url = server_url_base + "fota.php"
#url = "http://klingsor.uedasoft.com/tools/151024/fota.php"

serialid = gs.get_serialnumber()
try:
  payload = {'serial_id': serialid}
#  payload = {'serial_id': '00000000790f4c7c'}
  r=requests.get(fota_url, params=payload, timeout=10, cert=os.path.dirname(os.path.abspath(__file__))+'/slider.pem', verify=False)
#	r=requests.get("http://klingsor.uedasoft.com/tools/151024/fota.php", params=payload, timeout=10)
  resp=json.loads(r.text)
  if resp['restart'] == "1":
    slider.msg_log("reboot.")
    subprocess.Popen(reboot, shell=True)
  elif resp['command']:
    slider.msg_log("command = "+resp['command'])
    subprocess.Popen(resp['command'], shell=True)
except IOError:
  slider.network_io_error_report()
except:
  slider.unknown_error_report()

slider.network_ok_report()
