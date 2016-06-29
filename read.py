# coding:utf-8 Copy Right Atelier Grenouille © 2015 -
#
# require: 'usbrh' 
# http://www.infiniteloop.co.jp/blog/2013/02/raspberrypitem/
import os
import sys
#sys.path.append('/home/pi/SCRIPT')
import inspect
import traceback
import subprocess
import datetime
import importlib
import logging
import videodevices
import getserialnumber as gs
import pytoml as toml
#with open(os.path.dirname(__file__)+'/config.toml', 'rb') as fin:
with open('/home/pi/SCRIPT/config.toml', 'rb') as fin:
  config = toml.load(fin)

serialid = gs.get_serialnumber()

# ログファイルの設定
#logging.basicConfig(format='%(asctime)s %(filename)s %(lineno)d %(levelname)s %(message)s',filename=ini.get("log", "log_file"),level=logging.DEBUG)
logging.basicConfig(format='%(asctime)s %(filename)s %(lineno)d %(levelname)s %(message)s',filename='/home/pi/LOG/read.log',level=logging.DEBUG)

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

try:
  ############################################################
  # sensors
  #
  msg_log("read.py started.")

  for sensor_name, sensor_settings in config["sensors"].items():
    msg_log(sensor_name)
# road reader.
    reader = importlib.import_module(sensor_name)
    value = reader.read()

    datas = sensor_settings['data']
    for data in datas:
      msg_log(data[2])
      if data[2]: # Send
      # read specified sender.
        sender = importlib.import_module(data[2])
        sender.send(serialid, data[0], value[data[0]]) # serialid, name, value
      msg_log(data[3])
      if data[3]: # Save
      # read specified saver.
        saver = importlib.import_module(data[3])
        saver.save(serialid, data[0], value[data[0]]) # serialid, name, value

  ############################################################
  # image
  #
  for imagedevice_name, data in config["imaging"].items():
    imagedevice_settings = data["data"]
    msg_log( imagedevice_name)
    if imagedevice_name == 'uvc': # USB カメラなら
      devices = []
      d = datetime.datetime.today()
      now = d.strftime("%Y%m%d%H%M%S")
      if imagedevice_settings[1] == "one":
        devices = ["video0"]
      elif imagedevice_settings[1] == "all":
        # UVC カメラデバイスの数だけ
        devices = videodevices.videodevices_basename()
      for videodevice in devices:
        videodevice_now = datetime.datetime.today().strftime("%Y%m%d%H%M%S")
        filepath = '/tmp/'+now+'.jpg'
        msg_log( filepath)
#      command_str = 'fswebcam '+filepath+' -d /dev/'+videodevice+' -S 20 -r 640x480'
        command_str = 'fswebcam '+filepath+' -d /dev/'+videodevice+' -S 20 -r 320x240'
        msg_log( command_str)
        p = subprocess.check_call(command_str, shell=True)
        if imagedevice_settings[2]: # Send
        # read specified sender.
          msg_log(imagedevice_settings[2])
          sender = importlib.import_module(imagedevice_settings[2])
          sender.send(serialid, filepath, videodevice) # serialid, name, value
        if imagedevice_settings[3]: # Save
        # read specified saver.
          msg_log(imagedevice_settings[3])
          saver = importlib.import_module(imagedevice_settings[3])
          saver.save(serialid, videodevice, filepath) # serialid, device, picfilepath

  msg_log("read.py ended.")
except IOError:
  info=sys.exc_info()
  msg_err_log ("IOError:"+ traceback.format_exc(info[0]))
  msg_err_log (traceback.format_exc(info[1]))
  msg_err_log (traceback.format_exc(info[2]))
  inc_file_ioerror()
except:
  info=sys.exc_info()
  msg_err_log ("Unexpected error:"+ traceback.format_exc(info[0]))
  msg_err_log (traceback.format_exc(info[1]))
  msg_err_log (traceback.format_exc(info[2]))

