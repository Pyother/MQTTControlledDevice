# -*- coding: utf-8 -*-

import paho.mqtt.client as mqtt
from drive import drive
from iwconfig import get_signal_level
import serial
from time import sleep
import threading

DENSITY_MEASUREMENT = False
WIFI_MEASUREMENT = False

def on_connect(client, userdata, flags, rc): 
	print("Connected with result code "+str(rc))
	client.subscribe("AreaExplorer")

def on_message(client, userdata, msg):
	global DENSITY_MEASUREMENT
	global WIFI_MEASUREMENT
	message = (str(msg.payload))
	print(message)

	if "speedtest" in message:
		print("→ WiFi test request received")
		string = "wifitest_callback|" + str(get_signal_level())
		client.publish(topic="AreaExplorer", payload=string)

	if "wifi_measurement_start" in message:
		print("→ WiFi measurement started")
		WIFI_MEASUREMENT = True

	if "wifi_measurement_stop" in message:
		print("→ WiFi measurement stopped")
		WIFI_MEASUREMENT = False

	if "drive" in message:
		print("→ Drive request received")
		direction = ((message.split(":")[2]).split('"')[0])
		print("Direction: ", direction)
		drive(direction)

	if "density_measurement_start" in message:
		print("→ Density measurement started")
		DENSITY_MEASUREMENT = True

	if "density_measurement_stop" in message:
		print("→ Density measurement stopped")
		DENSITY_MEASUREMENT = False

def mqtt_loop():

	client.connect("test.mosquitto.org", 1883, 60)
	client.loop_forever()

def wifi_measurement_loop():

	while True:
		if WIFI_MEASUREMENT == True:
			string = "wifi_measurement_callback|" + str(get_signal_level())
			client.publish(topic="AreaExplorer", payload=string)
			sleep(0.5)

def density_measurement_loop():

	while True:
		if DENSITY_MEASUREMENT and ser.in_waiting > 0:
			line = ser.readline().decode('utf-8').rstrip()
			print(line)
			string = "density_measurement_callback|" + line
			client.publish(topic="AreaExplorer", payload=str(string))

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

ser = serial.Serial('/dev/ttyUSB0', 9600, timeout=1)
ser.reset_input_buffer()

density_measurement_thread = threading.Thread(target=density_measurement_loop)
density_measurement_thread.start()

wifi_measurement_thread = threading.Thread(target=wifi_measurement_loop)
wifi_measurement_thread.start()

mqtt_loop()




