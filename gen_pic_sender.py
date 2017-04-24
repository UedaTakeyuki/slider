# coding:utf-8 Copy Right Atelier Grenouille © 2015 -
#
# require: 'usbrh' 
# http://www.infiniteloop.co.jp/blog/2013/02/raspberrypitem/
import os
import sys
import datetime 
import locale 
import time 
import commands 
import subprocess
import logging
import traceback

# refered http://tdoc.info/blog/2014/09/25/mqtt_python.html
import paho.mqtt.client as mqtt
import json


import requests
import getserialnumber as gs
import getversion      as gv

import ConfigParser
import inspect

import slider_utils as slider

# 定数
configfile = os.path.dirname(os.path.abspath(__file__))+'/gen_pic_sender.ini'
reboot = 'sudo reboot'
network_restart = 'sudo service networking restart'
public_serialid = '0000000000000000'

# グローバル
g_count_of_file_ioerrors=0   # File IOERROR の回数。３回連続する場合、再起動する
g_count_of_network_ioerrors=0   # Network IOERROR の回数。３回連続する場合、再起動する

# 設定の取得
ini = ConfigParser.SafeConfigParser()
ini.read(configfile) #繰り返し毎に設定を取得
server_url_base = ini.get("server", "url_base")

# 設定値に依存する定数
url_data = server_url_base + 'postdata.php'

# ログファイルの設定
#logging.basicConfig(format='%(asctime)s %(filename)s %(lineno)d %(levelname)s %(message)s',filename=ini.get("log", "log_file"),level=logging.DEBUG)

#def msg_log(msg_str):
#    print str(inspect.currentframe(1).f_lineno) + " " + msg_str
#    logging.info(str(inspect.currentframe(1).f_lineno) + " " + msg_str)

#def msg_err_log(msg_str):
#    print str(inspect.currentframe(1).f_lineno) + " " + msg_str
#    logging.error(str(inspect.currentframe(1).f_lineno) + " " + msg_str)

#def inc_file_ioerror():
#    global g_count_of_file_ioerrors
#    g_count_of_file_ioerrors += 1
#    if g_count_of_file_ioerrors == 3:
#        subprocess.Popen(reboot, shell=True)

#def dec_file_ioerror():
#    global g_count_of_file_ioerrors
#    if g_count_of_file_ioerrors > 0:
#        g_count_of_file_ioerrors -= 1

#def inc_network_ioerror():
#    global g_count_of_network_ioerrors
#    g_count_of_network_ioerrors += 1
#    if g_count_of_network_ioerrors == 3:
#        g_count_of_network_ioerrors = 0
#        subprocess.Popen(network_restart, shell=True)

#def dec_network_ioerror():
#    global g_count_of_network_ioerrors
#    if g_count_of_network_ioerrors > 0:
#        g_count_of_network_ioerrors -= 1

def send_data(payload, files):
    global ini
    if ini.get("send", "protocol") == "http":
#        r = requests.post(ini.get("server", "url_base") + 'postpic.php', data=payload, files=files, timeout=10, verify=False)
        r = requests.post(ini.get("server", "url_base") + 'postpic.php', data=payload, files=files, timeout=10, cert=os.path.dirname(os.path.abspath(__file__))+'/slider.pem', verify=False)
        slider.msg_log("by http.")
    elif ini.get("send", "protocol") == "mqtt":
        mqttclient.publish(ini.get("mqtt", "topic"), json.JSONEncoder().encode(payload))
        slider.msg_log("by mqtt.")

#serialid = gs.get_serialnumber()
#msg_log("serialid=" + serialid)
#version  = gv.get_version()
#msg_log("version=" + version)

# mqtt
if ini.get("send", "protocol") == "mqtt":
    mqtt_id = ini.get("mqtt", "id_base")+serialid
    mqttclient = mqtt.Client(client_id=mqtt_id, clean_session=True, protocol=mqtt.MQTTv311)
    slider.msg_log("id = " + mqtt_id)
    #client.username_pw_set(USERNAME, PASSWORD)
    mqtt_host = ini.get("mqtt", "host")
    mqttclient.connect(mqtt_host)
    slider.msg_log("host = " + mqtt_host)


def send(serialid, filepath, device):
  global ini, public_serialid
  try:
    slider.msg_log ( "start sending...")
    if ini.get("monitor", "mode") == "public":
      # public mode, so use public_serialid
      serialid = public_serialid
    now = datetime.datetime.now() # 時刻の取得
    now_string = now.strftime("%Y/%m/%d %H:%M:%S")
    files = {'upfile': open(filepath, 'rb')}
    payload = {'serial_id': serialid, 'device': device, 'datetime': now_string}
    send_data(payload, files)
#    comand_str = 'curl --insecure -k -F "upfile=@' + filepath + '" -F "serial_id='+serialid+ '" -F "device='+device+'" '+requests.post(ini.get("server", "url_base")) + 'postpic.php'+ '--retry 30'
#    print command_str
#    p = subprocess.check_call(command_str, shell=True)
    slider.msg_log ( "end sending...")
    slider.network_ok_report()
  except IOError:
#    slider.io_error_report()
    slider.network_io_error_report()
  except:
    slider.unknown_error_report()
