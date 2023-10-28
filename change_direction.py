#!/usr/bin/env python3

import serial
from time import sleep

def turn(direction):

        ser = serial.Serial('/dev/ttyUSB0', 9600, timeout=1)
        ser.reset_input_buffer()

        counter = 0

        while (counter < 2):

                if direction == 'right':
                        ser.write(b"#")
                if direction == 'left':
                        ser.write(b"$")
                if direction == 'initial':
                        ser.write(b"*")

                line = ser.readline().decode('utf-8').rstrip()
                sleep(0.65)
                counter = counter + 1
