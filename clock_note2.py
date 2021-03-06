# coding:utf-8 Copy Right Atelier Ueda © 2016 -
#
# i2c_lcd install: http://think-bowl.com/raspberry-pi/installing-the-think-bowl-i2c-libraries-for-python/
# i2c_lcd usage: http://think-bowl.com/raspberry-pi/i2c-python-library-lcd-with-the-raspberry-pi/
import os
import sys
#sys.path.append("/home/osmc/MySCRIPT")
#sys.path.append("/home/osmc/MySCRIPT/quick2wire-python-api")
#sys.path.append(os.getcwd()+"/vendor/quick2wire-python-api/quick2wire")
sys.path.append(os.path.dirname(os.path.abspath(__file__))+"/vendor")
#from i2clibraries import i2c_lcd
#import quick2wire
import datetime
import time
import subprocess
import logging
import traceback
import inspect
import requests
import configparser
#import grequests
import gc_ssd1306

# 定数
configfile = os.path.dirname(os.path.abspath(__file__))+'/clock_note.ini'

# 設定の取得
ini = configparser.SafeConfigParser()
ini.read(configfile)
p = subprocess.Popen( os.path.dirname(os.path.abspath(__file__))+"/geti2caddress.sh ", stdout=subprocess.PIPE, shell=True)
i2c_addr = p.stdout.readline().strip().decode('utf-8')

logging.basicConfig(format='%(asctime)s %(filename)s %(lineno)d %(levelname)s %(message)s',filename='/home/pi/LOG/clock_note.engine.log',level=logging.DEBUG)
lcd = gc_ssd1306.ssd1306()
#lcd = i2c_lcd.i2c_lcd(int("0x" + i2c_addr,0),0, 2, 1, 0, 4, 5, 6, 7, 3)
def msg_log(msg_str):
	print (str(inspect.currentframe().f_lineno) + " " + msg_str)
	logging.info(str(inspect.currentframe().f_lineno) + " " + msg_str)

def msg_err_log(msg_str):
	print (str(inspect.currentframe().f_lineno) + " " + msg_str)
	logging.error(str(inspect.currentframe().f_lineno) + " " + msg_str)

def say(phrase):
	try:
	#p = subprocess.Popen("/home/pi/install/aquestalkpi/AquesTalkPi "+str+" | aplay",
	#p = subprocess.check_call('sudo sh -c "/home/pi/install/aquestalkpi/AquesTalkPi '+str+'| aplay"',
		#command = '/usr/bin/curl -F "phrase='+phrase.decode('utf-8')+'" localhost/say.php'
#		command = '/usr/bin/curl -F "phrase='+phrase+'" localhost/say.php'
#		command_str = command.encode('utf-8')
#		print (command_str)
		if ini.get("path", "say_path"): # settings is NOT null then
			payload = {'phrase': phrase}
			#r = requests.post('http://localhost/say.php', data=payload, timeout=10, verify=False)
	#		r = requests.post(ini.get("path", "say_path"), data=payload, timeout=10, verify=False)
#		urls = ['http://localhost/say.php']
#		rs = (grequests.post('http://localhost/say.php', data=payload, timeout=10, verify=False) for u in urls)
#		grequests.map(rs)
		#print (command)
#		p = subprocess.Popen(command,
#		p = subprocess.Popen(command_str,
#												stdout=subprocess.PIPE,
#												shell=True)
	except:
		msg_err_log(traceback.format_exc())
#		info=sys.exc_info()
#		msg_err_log ("Unexpected error:"+ traceback.format_exc(info[0]))
#		msg_err_log (traceback.format_exc(info[1]))
#		msg_err_log (traceback.format_exc(info[2]))

def current_ip():
	p = subprocess.Popen("hostname -I",
												stdout=subprocess.PIPE,
												shell=True)
	result = p.stdout.readline().strip()
	print (result)
	return result

def show_ip(sec):
	global lcd
	p = subprocess.Popen("hostname -I",
												stdout=subprocess.PIPE,
												shell=True)
	ip = p.stdout.readline().strip().decode('utf-8')
	ips = ip.split(".")
	lcd.set("IP: "+ips[0]+".",".".join(ips[1:4]))
	lcd.scroll()
#	lcd.home()
#	lcd.clear()
#	lcd.setPosition(1,0)
#	lcd.writeString("IP:")
#	lcd.setPosition(2,0)
#	lcd.writeString(p.stdout.readline().strip().decode('utf-8'))
	time.sleep(sec)

def show_temp(sec):
	global lcd
#	p = subprocess.Popen("tail -n 1 /boot/DATA/log/temp.csv",
	p = subprocess.Popen("tail -n 1 "+ini.get("data", "temp_path")+"/temp.csv",
												stdout=subprocess.PIPE,
												shell=True)
#	result = p.stdout.readline().strip().decode('utf-8').split(',')
	#result = p.stdout.readline().strip().decode('utf-8','ignore').split(',')
	result = p.stdout.readline().strip().split(',')
#	lcd.home()
#	lcd.clear()
#	lcd.writeString("TEMP = " + result[1])
	lcd.set("temp: ",result[1])
	lcd.scroll()
	say("温度"+result[1]+"度")
	time.sleep(sec)

def show_humidity(sec):
	global lcd
#	p = subprocess.Popen("tail -n 1 /boot/DATA/log/humidity.csv",
	p = subprocess.Popen("tail -n 1 "+ini.get("data", "humidity_path")+"/humidity.csv",
												stdout=subprocess.PIPE,
												shell=True)
	#result = p.stdout.readline().strip().decode('utf-8').split(',')
	result = p.stdout.readline().strip().split(',')
	lcd.set("Humidity:",result[1])
	lcd.scroll()
#	lcd.home()
#	lcd.clear()
#	lcd.writeString("Humidity = " + result[1])
	say("湿度"+result[1]+"%")
	time.sleep(sec)

def show_humiditydeficit(sec):
	global lcd
#	p = subprocess.Popen("tail -n 1 /boot/DATA/log/humiditydeficit.csv",
	p = subprocess.Popen("tail -n 1 "+ini.get("data", "humiditydeficit_path")+"/humiditydeficit.csv",
												stdout=subprocess.PIPE,
												shell=True)
	#result = p.stdout.readline().strip().decode('utf-8').split(',')
	result = p.stdout.readline().strip().split(',')
	lcd.set("HumidDef:",result[1])
	lcd.scroll()
#	lcd.home()
#	lcd.clear()
#	lcd.writeString("HumidDef = " + result[1])
#	say("飽差"+result[1])
	time.sleep(sec)

def show_CO2(sec):
	global lcd
	if ini.get("data", "CO2_path"): # settings is NOT null then
	#	p = subprocess.Popen("tail -n 1 /boot/DATA/log/co2.csv",
		p = subprocess.Popen("tail -n 1 "+ini.get("data", "CO2_path")+"/CO2.csv",
													stdout=subprocess.PIPE,
													shell=True)
		#result = p.stdout.readline().strip().decode('utf-8').split(',')
		result = p.stdout.readline().strip().split(',')
		lcd.set("CO2: "+result[1],"")
		lcd.scroll()
#		lcd.home()
#		lcd.clear()
#		lcd.writeString("CO2 = " + result[1])
		say("二酸化炭素濃度"+result[1]+"ppmです")
		time.sleep(sec)
	else:
		pass
#		lcd.home()
#		lcd.clear()

def fork():
	pid = os.fork()
	if pid > 0:
		f = open('/var/run/clock_note.pid','w')
		f.write(str(pid)+"\n")
		f.close()
		sys.exit()

	if pid == 0:
		main()

def main():
	global lcd
#	lcd.backLightOn()
	now_str_prev = datetime.datetime.now().strftime('%m-%d %H:%M:%S')
	is_said = False
	while True:
		now = datetime.datetime.now()
		now_str = datetime.datetime.now().strftime('%m-%d %H:%M:%S')
		now_date = datetime.datetime.now().strftime('%m-%d')
		now_time = datetime.datetime.now().strftime('%H:%M:%S')
		
		if (now.second == 1):
#			pass
			if not is_said:
				say(str(now.hour) + "時" + str(now.minute) + "分です")
				is_said = True
		if (now.second == 2):
			is_said = False
		
		if (datetime.datetime.now().second == 31):
			show_ip(2)
#			show_temp(2)
			show_temp(3) # openjtalk が間に合わない
			show_humidity(2)
			show_humiditydeficit(2)
			show_CO2(2)

		if not now_str == now_str_prev:
#			lcd.home()
#			lcd.writeString(now_str)
			lcd.set(now_date,now_time)
			lcd.scroll()
			now_str_prev = now_str

		time.sleep(0.1)

if __name__ == '__main__':
	fork()