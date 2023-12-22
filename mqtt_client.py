# -*- coding: utf-8 -*-

import paho.mqtt.client as mqtt
from drive import drive
from iwconfig import get_signal_level
import serial
from time import sleep
import threading

DENSITY_MEASUREMENT = False

def on_connect(client, userdata, flags, rc): 
	print("Connected with result code "+str(rc))
	client.subscribe("AreaExplorer")

def on_message(client, userdata, msg):
	global DENSITY_MEASUREMENT
	message = (str(msg.payload))
	print(message)

	if "speedtest" in message:
		print("→ Wifi test request received")
		string = "wifitest_callback|" + str(get_signal_level())
		client.publish(topic="AreaExplorer", payload=string)

	if "drive" in message:
		print("→ Drive request received")
		direction = ((message.split(":")[2]).split('"')[0])
		print("Direction: ", direction)
		drive(direction)

	if "density_measurement_start" in message:
		print("→ Density measurement started")
		DENSITY_MEASUREMENT = True

		# client.publish(topic="AreaExplorer", payload=str(carbon_monoxide_measurement()))

	if "density_measurement_stop" in message:
		print("→ Density measurement stopped")
		DENSITY_MEASUREMENT = False

def mqtt_loop():

	client.connect("test.mosquitto.org", 1883, 60)
	client.loop_forever()

def density_measurement_loop():

	while True:
		if DENSITY_MEASUREMENT and ser.in_waiting > 0:
			line = ser.readline().decode('utf-8').rstrip()
			print(line)
			client.publish(topic="AreaExplorer", payload=str(line))


client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

ser = serial.Serial('/dev/ttyUSB0', 9600, timeout=1)
ser.reset_input_buffer()

mqtt_thread = threading.Thread(target=mqtt_loop)
mqtt_thread.start()

density_measurement_loop()




