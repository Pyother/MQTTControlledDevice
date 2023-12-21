# -*- coding: utf-8 -*-

import paho.mqtt.client as mqtt
from drive import drive
from iwconfig import get_signal_level
import serial
import asyncio

DENSITY_MEASUREMENT = False

def on_connect(client, userdata, flags, rc): 
	print("Connected with result code "+str(rc))
	client.subscribe("AreaExplorer")

def on_message(client, userdata, msg):
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

async def measurement_loop():
	pass

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect("test.mosquitto.org", 1883, 60)
client.loop_forever()



