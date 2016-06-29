# -*- coding: utf-8 -*-
import commands

script='/home/pi/SCRIPT/getversion.sh'

def get_version():
    version = commands.getstatusoutput(script)
    return version[1]

if __name__ == '__main__':
    print get_version()
