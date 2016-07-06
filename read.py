# coding:utf-8 Copy Right Atelier Grenouille © 2015 -
#
import os
import sys
#import inspect
#import traceback
import subprocess
import datetime
import importlib
#import logging
import videodevices
import slider_utils as slider
import getserialnumber as gs
import pytoml as toml
with open(os.path.dirname(os.path.abspath(__file__))+'/config.toml', 'rb') as fin:
  config = toml.load(fin)

serialid = gs.get_serialnumber()


def read():
  try:
    ############################################################
    # sensors
    #
    slider.msg_log("read.py started.")

    for sensor_name, sensor_settings in config["sensors"].items():
      slider.msg_log(sensor_name)

      # road reader.
      reader = importlib.import_module(sensor_name)
      value = reader.read()

      datas = sensor_settings['data']
      for data in datas:
        slider.msg_log(data[2])
        if data[2]: # Send
          # read specified sender.
          sender = importlib.import_module(data[2])
          sender.send(serialid, data[0], value[data[0]]) # serialid, name, value
        slider.msg_log(data[3])
        if data[3]: # Save
          # read specified saver.
          saver = importlib.import_module(data[3])
          saver.save(serialid, data[0], value[data[0]]) # serialid, name, value

    ############################################################
    # image
    #
    for imagedevice_name, data in config["imaging"].items():
      imagedevice_settings = data["data"]
      slider.msg_log( imagedevice_name)
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
          slider.msg_log( filepath)
          command_str = 'fswebcam '+filepath+' -d /dev/'+videodevice+' -S 20 -r 320x240'
          slider.msg_log( command_str)
          p = subprocess.check_call(command_str, shell=True)
          if imagedevice_settings[2]: # Send
            # read specified sender.
            slider.msg_log(imagedevice_settings[2])
            sender = importlib.import_module(imagedevice_settings[2])
            sender.send(serialid, filepath, videodevice) # serialid, name, value
          if imagedevice_settings[3]: # Save
            # read specified saver.
            slider.msg_log(imagedevice_settings[3])
            saver = importlib.import_module(imagedevice_settings[3])
            saver.save(serialid, videodevice, filepath) # serialid, device, picfilepath

    slider.msg_log("read.py ended.")
  except IOError:
    slider.io_error_report()
  except:
    slider.unknown_error_report()

if __name__ == '__main__':
  read()
