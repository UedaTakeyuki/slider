# -*- coding: utf-8 -*-
import commands
import subprocess
import logging

check_script='ps -aef | grep gal4.py | grep -v grep | grep -v kick | wc -l'
check2_script='ps -aef | grep clock_note.py | grep -v grep | grep -v kick | wc -l'
gal3_script='sudo python /home/pi/SCRIPT/gal4.py &'
logfilename = '/home/pi/LOG/helth.log'
logging.basicConfig(format='%(asctime)s %(filename)s %(levelname)s %(message)s',filename=logfilename,level=logging.DEBUG)

def check():
    num = commands.getstatusoutput(check_script)
    return num[1]

def check2():
    num = commands.getstatusoutput(check2_script)
    return num[1]

if __name__ == '__main__':
    num = check()
    print num
    if num == "0":
        logging.info("### gal4 kicked! ###")
        p = subprocess.Popen(gal3_script, shell=True)
        # commands.getstatusoutput(gal3_script)
    num = check()
    print num

    num = check2()
    print num
    if num == "0":
        logging.info("### clock_note kicked! ###")
        p = subprocess.Popen("sudo python3 /home/pi/SCRIPT/clock_note.py &", shell=True)
        # commands.getstatusoutput(gal3_script)
    num = check()
    print num
