# -*- coding: utf-8 -*-

import RPi.GPIO as GPIO
import time
from servo import turn

# Ustawienie pinów dla L298N
IN1 = 17
IN2 = 18
IN3 = 22
IN4 = 23

# Inicjalizacja GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(IN1, GPIO.OUT)
GPIO.setup(IN2, GPIO.OUT)
GPIO.setup(IN3, GPIO.OUT)
GPIO.setup(IN4, GPIO.OUT)

# Funkcja do przodu
def north():
	GPIO.output(IN1, GPIO.HIGH)
	GPIO.output(IN2, GPIO.LOW)
	GPIO.output(IN3, GPIO.HIGH)
	GPIO.output(IN4, GPIO.LOW)

# Funkcja do tyłu
def south():
	GPIO.output(IN1, GPIO.LOW)
	GPIO.output(IN2, GPIO.HIGH)
	GPIO.output(IN3, GPIO.LOW)
	GPIO.output(IN4, GPIO.HIGH)

# Funkcja do zatrzymania silników
def stop():
	GPIO.output(IN1, GPIO.LOW)
	GPIO.output(IN2, GPIO.LOW)
	GPIO.output(IN3, GPIO.LOW)
	GPIO.output(IN4, GPIO.LOW)

def drive(direction):

	if direction == "north":
		turn('initial')
		north()
		time.sleep(0.5)
		stop()

	if direction == "south":
		turn('initial')
		south()
		time.sleep(0.5)
		stop()

	if direction == "northwest":
		turn('left')
		north()
		time.sleep(0.5)
		stop()

	if direction == "northeast":
		turn('right')
		north()
		time.sleep(0.5)
		stop()

	if direction == "southwest":
		turn('left')
		south()
		time.sleep(0.5)
		stop()

	if direction == "southeast":
		turn('right')
		south()
		time.sleep(0.5)
		stop()
