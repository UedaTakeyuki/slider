# coding:utf-8 Copy Right Atelier UEDA © 2016 -
import os
import commands
import subprocess
import logging

check_script='ps -aef | grep water_leak_detecte.py | grep -v grep | grep -v kick | wc -l'
check2_script='ps -aef | grep clock_note.py | grep -v grep | grep -v kick | wc -l'
gal3_script='sudo python /home/pi/SCRIPT/gal4.py &'
clock_note_script='sudo python3 '+os.path.dirname(os.path.abspath(__file__))+'/clock_note.py &'
water_leak_detecte_script='python '+os.path.dirname(os.path.abspath(__file__))+'/water_leak_detecte.py > /dev/null 2>&1 &'
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
        logging.info("### water_leak_detecte kicked! ###")
        p = subprocess.Popen(water_leak_detecte_script, shell=True)

    num = check2()
    print num
    if num == "0":
        logging.info("### clock_note kicked! ###")
        p = subprocess.Popen(clock_note_script, shell=True)
#        pass
