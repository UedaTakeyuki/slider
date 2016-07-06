# -*- coding: utf-8 -*-
import os
import commands

script=os.path.dirname(os.path.abspath(__file__))+'/getserialnumber.sh'

def get_serialnumber():
    serial_id = commands.getstatusoutput(script)
    return serial_id[1]

if __name__ == '__main__':
    print get_serialnumber()
