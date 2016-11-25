# -*- coding: utf-8 -*-
# refer https://github.com/guyc/py-gaugette
#
# Copy Right Atelier Ueda © 2016 -

import gaugette.ssd1306
import time

ROWS = 32

RESET_PIN = 15
DC_PIN    = 16


class ssd1306:
  def __init__(self):
    self.led = gaugette.ssd1306.SSD1306(reset_pin=RESET_PIN, dc_pin=DC_PIN, rows=ROWS, cols=128)
    self.led.begin()
    self.led.clear_display()
    self.led.display()
    self.prev_text1 = ""
    self.prev_text2 = ""

  def set(self, text1, text2):
    self.led.clear_display()
    self.led.draw_text2(0,0,self.prev_text1,2)
    self.led.draw_text2(0,16,self.prev_text2,2)
    self.led.draw_text2(0,32,text1,2)
    self.led.draw_text2(0,48,text2,2)
    self.prev_text1 = text1
    self.prev_text2 = text2
    self.led.display()
#    time.sleep(0.2)

  def scroll(self):
    offset = 0 # flips between 0 and 32 for double buffering
    for i in range(0,32):
      offset = (offset + 1) % 64
      self.led.command(self.led.SET_START_LINE | offset)
      time.sleep(0.01)
