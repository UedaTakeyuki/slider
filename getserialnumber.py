# -*- coding: utf-8 -*-
import commands

script='/home/pi/SCRIPT/getserialnumber.sh'

def get_serialnumber():
    serial_id = commands.getstatusoutput(script)
    return serial_id[1]

if __name__ == '__main__':
    print get_serialnumber()
