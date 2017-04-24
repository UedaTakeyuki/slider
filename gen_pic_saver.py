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

import slider_utils as slider

# 定数
configfile = os.path.dirname(os.path.abspath(__file__))+'/gen_pic_saver.ini'
reboot = 'sudo reboot'
network_restart = 'sudo service networking restart'

# グローバル
#g_count_of_file_ioerrors=0   # File IOERROR の回数。３回連続する場合、再起動する
#g_count_of_network_ioerrors=0   # Network IOERROR の回数。３回連続する場合、再起動する

# 設定の取得
ini = ConfigParser.SafeConfigParser()
ini.read(configfile) #繰り返し毎に設定を取得

# データ保存フォルダ
data_path = ini.get("save", "data_path")


# ログファイルの設定
#logging.basicConfig(format='%(asctime)s %(filename)s %(lineno)d %(levelname)s %(message)s',filename=ini.get("log", "log_file"),level=logging.DEBUG)

'''def msg_log(msg_str):
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
'''

def if_not_exist_then_make_folder(device, today):
    device_path = data_path+'/'+device
    if not os.path.isdir(device_path):
        os.mkdir(device_path)
    today_path = device_path+'/'+today
    if not os.path.isdir(today_path):
        os.mkdir(today_path)

def save(serialid, device, picfilepath):
    try:
        slider.msg_log('start saving...')
        today = datetime.datetime.now() # 時刻の取得
        today_string = today.strftime("%Y%m%d")
        savedfilepath = data_path+'/'+device+'/'+today_string+'/'+os.path.basename(picfilepath)
        slider.msg_log('savedfilepath = '+savedfilepath)
        if_not_exist_then_make_folder(device, today_string)
        shutil.move(picfilepath, savedfilepath)
        slider.msg_log('end saving...')
    except IOError:
        slider.file_io_error_report()
    except:
        slider.unknown_error_report()
    slider.file_ok_report()


