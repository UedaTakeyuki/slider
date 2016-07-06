# -*- coding: utf-8 -*-
import os
import commands

script=os.path.dirname(os.path.abspath(__file__))+'/getversion.sh'

def get_version():
    version = commands.getstatusoutput(script)
    return version[1]

if __name__ == '__main__':
    print get_version()
