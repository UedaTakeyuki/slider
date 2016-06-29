# coding:utf-8
# Copy Right Atelier Ueda🐸 © 2016 -
#
# return:  ["/dev/video0", "/dev/video1", ...]

import pprint
import subprocess
import re

def videodevices():
    result = []
    p = subprocess.Popen("ls /dev/video*", stdout=subprocess.PIPE, shell=True)
    for e in p.stdout.readlines():
        result.append(e.strip())
#    result = p.stdout.readline().strip()
    return result

def videodevices_basename():
    result = []
    p = subprocess.Popen("ls /dev/video*", stdout=subprocess.PIPE, shell=True)
    for e in p.stdout.readlines():
        result.append(re.sub(r'/dev/', '', e.strip()))
#    result = p.stdout.readline().strip()
    return result

def videodevices_numbers():
    result = []
    p = subprocess.Popen("ls /dev/video*", stdout=subprocess.PIPE, shell=True)
    for e in p.stdout.readlines():
        result.append(re.sub(r'/dev/video', '', e.strip()))
#    result = p.stdout.readline().strip()
    return result

if __name__ == '__main__':
    pprint.pprint (videodevices())
    pprint.pprint (videodevices_basename())
    pprint.pprint (videodevices_numbers())
