# coding:utf-8
# Copy Right Atelier Ueda🐸 © 2016 -
#
# return:  ["/dev/video0", "/dev/video1", ...]

import subprocess
import re
import time

class LED:
    def __init__(self):
        pass

    def __del__(self):
        pass

    def __str__(self):
        pass

    # Start to use LED.
    def use(self, number): #number: LED number 0 or 1
        # release trigger for get control.
        command_str = 'sudo sh -c "echo none > /sys/class/leds/led' + str(number) +'/trigger"'
        p = subprocess.check_call(command_str, shell=True)

    # End to use LED.
    def release(self, number): #number: LED number 0 or 1
        # back to default.
        if number == 0: 
            trigger_str = "mmc0"
        elif number == 1:
            trigger_str = "input"
        command_str = 'sudo sh -c "echo ' + trigger_str + ' > /sys/class/leds/led' + str(number) +'/trigger"'
        p = subprocess.check_call(command_str, shell=True)

    # Turn LED on.
    def on(self, number): #number: LED number 0 or 1
        command_str = 'sudo sh -c "echo 1 > /sys/class/leds/led' + str(number) +'/brightness"'
        p = subprocess.check_call(command_str, shell=True)

    # Turn LED on.
    def off(self, number): #number: LED number 0 or 1
        command_str = 'sudo sh -c "echo 0 > /sys/class/leds/led' + str(number) +'/brightness"'
        p = subprocess.check_call(command_str, shell=True)

    def short(self, number): #number: LED number 0 or 1
        self.on(number)
        time.sleep(0.1)
        self.off(number)
        time.sleep(0.1)

    def long(self, number): #number: LED number 0 or 1
        self.on(number)
        time.sleep(0.3)
        self.off(number)
        time.sleep(0.1)

    def inter_char(self, number): #number: LED number 0 or 1
        self.off(number)
        time.sleep(0.2)

    def inter_word(self, number): #number: LED number 0 or 1
        self.off(number)
        time.sleep(0.6)

    #########################################################
    #
    # Morse code 
    #
    #
    # A   ・－
    # B   －・・・
    # C   －・－・
    # D   －・・
    # E   ・
    # F   ・・－・
    # G   －－・
    # H   ・・・・
    # I   ・・
    # J   ・－－－
    # K   －・－
    # L   ・－・・
    # M   －－
    # N   －・
    # O   －－－
    # P   ・－－・
    # Q   －－・－
    # R   ・－・
    # S   ・・・
    # T   －
    # U   ・・－
    # V   ・・・－
    # W   ・－－
    # X   －・・－
    # Y   －・－－
    # Z   －－・・
    #########################################################

    def A(self, number): #number: LED number 0 or 1
        # A   ・－
        led.short(number)
        led.long(number)

    def B(self, number): #number: LED number 0 or 1
        # B   －・・・
        led.long(number)
        led.short(number)
        led.short(number)
        led.short(number)
        
    def C(self, number): #number: LED number 0 or 1
        # C   －・－・
        led.long(number)
        led.short(number)
        led.long(number)
        led.short(number)
        
    def D(self, number): #number: LED number 0 or 1
        # D   －・・
        led.long(number)
        led.short(number)
        led.short(number)
        
    def E(self, number): #number: LED number 0 or 1
        # E   ・
        led.short(number)
        
    def F(self, number): #number: LED number 0 or 1
        # F   ・・－・
        led.short(number)
        led.short(number)
        led.long(number)
        led.short(number)
        
    def G(self, number): #number: LED number 0 or 1
        # G   －－・
        led.long(number)
        led.long(number)
        led.short(number)
        
    def H(self, number): #number: LED number 0 or 1
        # H   ・・・・
        led.short(number)
        led.short(number)
        led.short(number)
        led.short(number)
        
    def I(self, number): #number: LED number 0 or 1
        # I   ・・
        led.short(number)
        led.short(number)
        
    def J(self, number): #number: LED number 0 or 1
        # J   ・－－－
        led.short(number)
        led.long(number)
        led.long(number)
        led.long(number)
        
    def K(self, number): #number: LED number 0 or 1
        # K   －・－
        led.long(number)
        led.short(number)
        led.long(number)
        
    def L(self, number): #number: LED number 0 or 1
        # L   ・－・・
        led.short(number)
        led.long(number)
        led.short(number)
        led.short(number)
        
    def M(self, number): #number: LED number 0 or 1
        # M   －－
        led.long(number)
        led.long(number)
        
    def N(self, number): #number: LED number 0 or 1
        # N   －・
        led.long(number)
        led.short(number)
        
    def O(self, number): #number: LED number 0 or 1
        # O   －－－
        led.long(number)
        led.long(number)
        led.long(number)
        
    def P(self, number): #number: LED number 0 or 1
        # P   ・－－・
        led.short(number)
        led.long(number)
        led.long(number)
        led.short(number)
        
    def Q(self, number): #number: LED number 0 or 1
        # Q   －－・－
        led.long(number)
        led.long(number)
        led.short(number)
        led.long(number)
        
    def R(self, number): #number: LED number 0 or 1
        # R   ・－・
        led.short(number)
        led.long(number)
        led.short(number)
        
    def S(self, number): #number: LED number 0 or 1
        # S   ・・・
        led.short(number)
        led.short(number)
        led.short(number)
        
    def T(self, number): #number: LED number 0 or 1
        # T   －
        led.long(number)

    def U(self, number): #number: LED number 0 or 1
        # U   ・・－
        led.short(number)
        led.short(number)
        led.long(number)

    def V(self, number): #number: LED number 0 or 1
        # V   ・・・－
        led.short(number)
        led.short(number)
        led.short(number)
        led.long(number)

    def W(self, number): #number: LED number 0 or 1
        # W   ・－－
        led.short(number)
        led.long(number)
        led.long(number)

    def X(self, number): #number: LED number 0 or 1
        # X   －・・－
        led.long(number)
        led.short(number)
        led.short(number)
        led.long(number)

    def Y(self, number): #number: LED number 0 or 1
        # Y   －・－－
        led.long(number)
        led.short(number)
        led.long(number)
        led.long(number)

    def Z(self, number): #number: LED number 0 or 1
        # Z   －－・・
        led.long(number)
        led.long(number)
        led.short(number)
        led.short(number)

if __name__ == '__main__':
    led = LED()
    print "green on."
    led.use(0)
    led.on(0)
    print "red on."
    led.use(1)
    led.on(1)
    print "green off."
    led.off(0)
    led.release(0)
    print "red off."
    led.off(1)
    led.release(1)

    time.sleep(1)

    led.use(0)
    led.S(0)
    led.inter_char(0)
    led.O(0)
    led.inter_char(0)
    led.S(0)
    led.inter_word(0)
