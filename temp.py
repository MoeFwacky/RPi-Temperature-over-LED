#! /usr/bin/python
import os
import time
import sys
sys.path.append('/storage/lib')
import RPi.GPIO as GPIO

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
#PWR =15
HOT =5
NOT =13
#GPIO.setup(PWR, GPIO.OUT)

GPIO.setup(HOT, GPIO.OUT)
HOT_LED = GPIO.PWM( HOT, 50)

GPIO.setup(NOT, GPIO.OUT)
NOT_LED = GPIO.PWM( NOT, 50)

#GPIO.output(PWR,True)
temperature = os.popen("cat /sys/class/thermal/thermal_zone0/temp").readline()
i = int(temperature)
s = str(i)
blue = int(s[0])
red = int(s[1])

def blink_blue():
                time.sleep(.1)
                NOT_LED.start(1)
                time.sleep(.1)
                NOT_LED.start(0)

def blink_red():
                time.sleep(.1)
                HOT_LED.start(1)
                time.sleep(.1)
                HOT_LED.start(0)

def led():
                for _ in range(blue):
                        blink_blue()
                for _ in range(red):
                        blink_red()
                return

while True:
#       print(f)
        led();
        time.sleep(2)
        temperature = os.popen("cat /sys/class/thermal/thermal_zone0/temp").readline()
        i = int(temperature)
        s = str(i)
        blue = int(s[0])
        red = int(s[1])
