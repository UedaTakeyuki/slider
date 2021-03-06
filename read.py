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

def is_rtmpbroadcast():
  p = subprocess.Popen("sudo ps -aef | grep rtmpbroadcast | grep -v grep | wc -l", stdout=subprocess.PIPE, shell=True)
  result = int(p.stdout.readline().strip())
  if result == 1:
    return True
  else:
    return False

def read():
  ############################################################
  # sensors
  #
  slider.msg_log("read.py started.")

  # rtmpbroadcast 中ならスキップ
  if is_rtmpbroadcast():
    slider.msg_log("conflict with rtmpbroadcast")
    return False

  for sensor_name, sensor_settings in config["sensors"].items():
    slider.msg_log(sensor_name)

    # road reader.
    reader = importlib.import_module(sensor_name)
    try:
      value = reader.read()
    except IOError:
      slider.io_error_report()
      continue
    except:
      slider.unknown_error_report()
      continue

    if (value is not None):
      datas = sensor_settings['data']
      for data in datas:
        slider.msg_log(data[2])
        if data[2]: # Send
          # read specified sender.
          try:
            sender = importlib.import_module(data[2])
            sender.send(serialid, data[0], value[data[0]]) # serialid, name, value
          except IOError:
            slider.io_error_report()
          except:
            slider.unknown_error_report()
        slider.msg_log(data[3])
        if data[3]: # Save
          # read specified saver.
          try:
            saver = importlib.import_module(data[3])
            saver.save(serialid, data[0], value[data[0]]) # serialid, name, value
          except IOError:
            slider.io_error_report()
          except:
            slider.unknown_error_report()

  ############################################################
  # image
  #
  for imagedevice_name, data in config["imaging"].items():
    imagedevice_settings = data["data"]
    slider.msg_log( imagedevice_name)
    if imagedevice_name == 'uvc': # USB カメラなら
      devices = []
#      d = datetime.datetime.today()
#      now = d.strftime("%Y%m%d%H%M%S")
      if imagedevice_settings[1] == "one":
        devices = ["video0"]
      elif imagedevice_settings[1] == "all":
        # UVC カメラデバイスの数だけ
        devices = videodevices.videodevices_basename()
      elif imagedevice_settings[1] == "dummy":
        # dummy 画像の取得
        devices = ["video0"]

      for videodevice in devices:
        # rtmpbroadcast 中ならスキップ
        # if is_rtmpbroadcast():
        #   continue

        videodevice_now = datetime.datetime.today().strftime("%Y%m%d%H%M%S")
        filepath = '/tmp/'+videodevice_now+'.jpg'
        slider.msg_log( filepath)
        if imagedevice_settings[1] == "dummy":
#          command_str = 'fswebcam '+filepath+' -d TEST -r 320x240'
          command_str = os.path.dirname(os.path.abspath(__file__))+'/photographier.sh '+filepath+' dummy 320x240'
        else:
#          command_str = 'fswebcam '+filepath+' -d /dev/'+videodevice+' -D 1 -S 20 -r 320x240'
          command_str = os.path.dirname(os.path.abspath(__file__))+'/photographier.sh '+filepath+' '+videodevice+' 320x240'
        slider.msg_log( command_str)
        try:
          p = subprocess.check_call(command_str, shell=True)
          slider.msg_log ('p = ' + str(p))
        except IOError:
          slider.io_error_report()
          continue
        except:
          slider.unknown_error_report()
          continue

        if imagedevice_settings[2]: # Send
          # read specified sender.
          slider.msg_log(imagedevice_settings[2])
          try:
            sender = importlib.import_module(imagedevice_settings[2])
            sender.send(serialid, filepath, videodevice) # serialid, name, value
          except IOError:
            slider.io_error_report()
          except:
            slider.unknown_error_report()

        if imagedevice_settings[3]: # Save
          # read specified saver.
          slider.msg_log(imagedevice_settings[3])
          try:
            saver = importlib.import_module(imagedevice_settings[3])
            saver.save(serialid, videodevice, filepath) # serialid, device, picfilepath
          except IOError:
            slider.io_error_report()
          except:
            slider.unknown_error_report()

        # 撮影画像を move しなかった場合は明に削除
        if os.path.exists(filepath):
          os.remove(filepath)

  slider.msg_log("read.py ended.")

if __name__ == '__main__':
  read()
