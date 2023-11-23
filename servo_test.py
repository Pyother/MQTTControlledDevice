# -*- coding: utf-8 -*-

import serial
import time

while True:
	ser = serial.Serial('/dev/ttyUSB0', 9600, timeout=1)
	ser.reset_input_buffer()	
	time.sleep(1)
        ser.write(b"#")
	time.sleep(2)
	ser.write(b"*")
