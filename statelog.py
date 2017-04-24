# coding:utf-8 Copy Right Atelier Grenouille © 2015 -
import os
import getserialnumber as gs

import ConfigParser
import logging
import subprocess
import requests
import datetime 

import slider_utils as slider

# 定数
configfile = os.path.dirname(os.path.abspath(__file__))+'/config.ini'
logfilename = '/home/pi/LOG/helth.log'
vmstd='vmstat | tail -n 1'

# 設定の取得
ini = ConfigParser.SafeConfigParser()
ini.read(configfile) #繰り返し毎に設定を取得
server_url_base = ini.get("server", "url_base")

# 設定値に依存する定数
url_data = server_url_base + 'postdata2.php'
serialid = gs.get_serialnumber()

now = datetime.datetime.now() # 時刻の取得
now_string = now.strftime("%Y/%m/%d %H:%M:%S")

# vmstat の取得
p = subprocess.Popen(vmstd, stdout=subprocess.PIPE, shell=True)
vmstat_result = p.stdout.readline().strip()

# ヘルスログファイルへの記録
logging.basicConfig(format='%(asctime)s %(filename)s %(levelname)s %(message)s',filename=logfilename,level=logging.DEBUG)
try:
  logging.info(vmstat_result)
except IOError:
  slider.file_io_error_report()
except:
  slider.unknown_error_report()
slider.file_ok_report()

# chlog への post
payload = {'serial_id': serialid, 'filename': 'chlog.txt', 'textstr': now_string+", "+vmstat_result}
try:
	r = requests.post(url_data, data=payload, timeout=10, cert=os.path.dirname(os.path.abspath(__file__))+'/slider.pem', verify=False)
except IOError:
  slider.network_io_error_report()
except:
  slider.unknown_error_report()
slider.network_ok_report()

### ↓↓↓ 2016.10.31 追加 ↓↓↓
# ls /dev/video* の取得
lsvideos = 'ls /dev/video*'
p = subprocess.Popen(lsvideos, stdout=subprocess.PIPE, shell=True)
lsvideos_result = p.stdout.read()
lsvideos_result = lsvideos_result.replace('/dev/video','')
lsvideos_result = lsvideos_result.replace('\n',', ')
#lsvideos_result = lsvideos_result.replace('\r','')

#videoslog への post
try:
  payload = {'serial_id': serialid, 'filename': 'videoslog.txt', 'textstr': now_string+", "+lsvideos_result}
  r = requests.post(url_data, data=payload, timeout=10, cert=os.path.dirname(os.path.abspath(__file__))+'/slider.pem', verify=False)
except IOError:
  slider.network_io_error_report()
except:
  slider.unknown_error_report()
slider.network_ok_report()

# reboot if number of video devices is not much.
import glob
reboot = 'sudo reboot'
#videodevices = os.listdir('/dev/video*')
videodevices = glob.glob('/dev/video*')
#if len(videodevices) < 9:
#	p = subprocess.Popen(reboot, stdout=subprocess.PIPE, shell=True)

