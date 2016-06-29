# coding:utf-8 Copy Right Atelier Grenouille © 2015 -
#
# require: 'usbrh' 
# http://www.infiniteloop.co.jp/blog/2013/02/raspberrypitem/
import os
import shutil

import sys
import datetime 
import locale 
import time 
import commands 
import subprocess
import logging
import traceback


import requests
import getserialnumber as gs
import getversion      as gv

import ConfigParser
import inspect

# 定数
configfile = '/home/pi/SCRIPT/gen_pic_saver.ini'
reboot = 'sudo reboot'
network_restart = 'sudo service networking restart'

# グローバル
g_count_of_file_ioerrors=0   # File IOERROR の回数。３回連続する場合、再起動する
g_count_of_network_ioerrors=0   # Network IOERROR の回数。３回連続する場合、再起動する

# 設定の取得
ini = ConfigParser.SafeConfigParser()
ini.read(configfile) #繰り返し毎に設定を取得

# データ保存フォルダ
data_path = ini.get("save", "data_path")


# ログファイルの設定
#logging.basicConfig(format='%(asctime)s %(filename)s %(lineno)d %(levelname)s %(message)s',filename=ini.get("log", "log_file"),level=logging.DEBUG)

def msg_log(msg_str):
    print str(inspect.currentframe(1).f_lineno) + " " + msg_str
    logging.info(str(inspect.currentframe(1).f_lineno) + " " + msg_str)

def msg_err_log(msg_str):
    print str(inspect.currentframe(1).f_lineno) + " " + msg_str
    logging.error(str(inspect.currentframe(1).f_lineno) + " " + msg_str)

def inc_file_ioerror():
    global g_count_of_file_ioerrors
    g_count_of_file_ioerrors += 1
    if g_count_of_file_ioerrors == 3:
        subprocess.Popen(reboot, shell=True)

def dec_file_ioerror():
    global g_count_of_file_ioerrors
    if g_count_of_file_ioerrors > 0:
        g_count_of_file_ioerrors -= 1

def inc_network_ioerror():
    global g_count_of_network_ioerrors
    g_count_of_network_ioerrors += 1
    if g_count_of_network_ioerrors == 3:
        g_count_of_network_ioerrors = 0
        subprocess.Popen(network_restart, shell=True)

def dec_network_ioerror():
    global g_count_of_network_ioerrors
    if g_count_of_network_ioerrors > 0:
        g_count_of_network_ioerrors -= 1

def send_data(payload):
    global ini
    if ini.get("send", "potocol") == "http":
        r = requests.post(ini.get("server", "url_base") + 'postdata.php', data=payload, timeout=10, verify=False)
        msg_log("by http.")
    elif ini.get("send", "potocol") == "mqtt":
        mqttclient.publish(ini.get("mqtt", "topic"), json.JSONEncoder().encode(payload))
        msg_log("by mqtt.")

#serialid = gs.get_serialnumber()
#msg_log("serialid=" + serialid)
#version  = gv.get_version()
#msg_log("version=" + version)

def if_not_exist_then_make_folder(device, today):
    device_path = data_path+'/'+device
    if not os.path.isdir(device_path):
        os.mkdir(device_path)
    today_path = device_path+'/'+today
    if not os.path.isdir(today_path):
        os.mkdir(today_path)

def save(serialid, device, picfilepath):
    msg_log('start saving...')
    today = datetime.datetime.now() # 時刻の取得
    today_string = today.strftime("%Y%m%d")
    savedfilepath = data_path+'/'+device+'/'+today_string+'/'+os.path.basename(picfilepath)
    msg_log('savedfilepath = '+savedfilepath)
    if_not_exist_then_make_folder(device, today_string)
    shutil.move(picfilepath, savedfilepath)
    msg_log('end saving...')

