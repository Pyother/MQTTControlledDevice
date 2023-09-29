# -*- coding: utf-8 -*-

from gpiozero import AngularServo
import time

servo = AngularServo(13, min_pulse_width=0.0005, max_pulse_width=0.0025)

while (True):
	servo.angle = 90
	time.sleep(2)
	servo.angle = 0 
	time.sleep(2)
	servo.angle = -90
	time.sleep(2)

