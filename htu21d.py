# -*- coding: utf-8 -*-
#
# For module GY-21, or sensor HTU21D
#
# refer https://cdn-shop.adafruit.com/datasheets/1899_HTU21D.pdf
# refer https://github.com/jasiek/HTU21D/blob/master/HTU21D.py
# 
# © Takeyuki UEDA 2018 - 

import smbus
import getrpimodel
import geti2caddress

# htu21d command
RDTEMP  = 0xE3
RDHUMID = 0xE5
RESET   = 0xFE

# select bus info
if getrpimodel.model() == "A+":
  i2c_bus = 0
else:
  i2c_bus = 1

# make smbus
bus = smbus.SMBus(i2c_bus)

class HTU21D:
	def __init__(self):
		# get i2c address of sensor
		self.I2C_ADDRESS = int(geti2caddress.addr(),16)

		# select bus info
		if getrpimodel.model() == "A+":
			self.I2C_BUS = 0
		else:
			self.I2C_BUS = 1

		# make smbus
		self.bus = smbus.SMBus(self.I2C_BUS)

	def temp(self):
		msb, lsb, crc = self.bus.read_i2c_block_data(self.I2C_ADDRESS, RDTEMP, 3)
		self.t = -46.85 + 175.72 * (msb * 256 + lsb) / 65536
		return self.t

	def humid(self):
		msb, lsb, crc = self.bus.read_i2c_block_data(self.I2C_ADDRESS, RDHUMID, 3)
		self.h = -6 + 125 * (msb * 256 + lsb) / 65536.0
		return self.h

h = HTU21D()

def read():
	result = {"temp":			('%.1f' % h.temp()),
						"humidity":	('%.1f' % h.humid())}
	return result

if __name__ == '__main__':
	print (read())