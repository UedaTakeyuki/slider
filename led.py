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
        self.short(number)
        self.long(number)

    def B(self, number): #number: LED number 0 or 1
        # B   －・・・
        self.long(number)
        self.short(number)
        self.short(number)
        self.short(number)
        
    def C(self, number): #number: self number 0 or 1
        # C   －・－・
        self.long(number)
        self.short(number)
        self.long(number)
        self.short(number)
        
    def D(self, number): #number: self number 0 or 1
        # D   －・・
        self.long(number)
        self.short(number)
        self.short(number)
        
    def E(self, number): #number: self number 0 or 1
        # E   ・
        self.short(number)
        
    def F(self, number): #number: self number 0 or 1
        # F   ・・－・
        self.short(number)
        self.short(number)
        self.long(number)
        self.short(number)
        
    def G(self, number): #number: self number 0 or 1
        # G   －－・
        self.long(number)
        self.long(number)
        self.short(number)
        
    def H(self, number): #number: self number 0 or 1
        # H   ・・・・
        self.short(number)
        self.short(number)
        self.short(number)
        self.short(number)
        
    def I(self, number): #number: self number 0 or 1
        # I   ・・
        self.short(number)
        self.short(number)
        
    def J(self, number): #number: self number 0 or 1
        # J   ・－－－
        self.short(number)
        self.long(number)
        self.long(number)
        self.long(number)
        
    def K(self, number): #number: self number 0 or 1
        # K   －・－
        self.long(number)
        self.short(number)
        self.long(number)
        
    def L(self, number): #number: self number 0 or 1
        # L   ・－・・
        self.short(number)
        self.long(number)
        self.short(number)
        self.short(number)
        
    def M(self, number): #number: self number 0 or 1
        # M   －－
        self.long(number)
        self.long(number)
        
    def N(self, number): #number: self number 0 or 1
        # N   －・
        self.long(number)
        self.short(number)
        
    def O(self, number): #number: self number 0 or 1
        # O   －－－
        self.long(number)
        self.long(number)
        self.long(number)
        
    def P(self, number): #number: self number 0 or 1
        # P   ・－－・
        self.short(number)
        self.long(number)
        self.long(number)
        self.short(number)
        
    def Q(self, number): #number: self number 0 or 1
        # Q   －－・－
        self.long(number)
        self.long(number)
        self.short(number)
        self.long(number)
        
    def R(self, number): #number: self number 0 or 1
        # R   ・－・
        self.short(number)
        self.long(number)
        self.short(number)
        
    def S(self, number): #number: self number 0 or 1
        # S   ・・・
        self.short(number)
        self.short(number)
        self.short(number)
        
    def T(self, number): #number: self number 0 or 1
        # T   －
        self.long(number)

    def U(self, number): #number: self number 0 or 1
        # U   ・・－
        self.short(number)
        self.short(number)
        self.long(number)

    def V(self, number): #number: self number 0 or 1
        # V   ・・・－
        self.short(number)
        self.short(number)
        self.short(number)
        self.long(number)

    def W(self, number): #number: self number 0 or 1
        # W   ・－－
        self.short(number)
        self.long(number)
        self.long(number)

    def X(self, number): #number: self number 0 or 1
        # X   －・・－
        self.long(number)
        self.short(number)
        self.short(number)
        self.long(number)

    def Y(self, number): #number: self number 0 or 1
        # Y   －・－－
        self.long(number)
        self.short(number)
        self.long(number)
        self.long(number)

    def Z(self, number): #number: self number 0 or 1
        # Z   －－・・
        self.long(number)
        self.long(number)
        self.short(number)
        self.short(number)

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
