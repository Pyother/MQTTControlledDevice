import paho.mqtt.client as mqtt
from wifitest import wifitest
# from drive import drive
from carbon_monoxide_measurement import carbon_monoxide_measurement
from methane_measurement import methane_measurement
import asyncio
import time
#from blink_led import blink_led
from speedtest import speedtest

def on_connect(client, userdata, flags, rc): 
    print("Connected with result code "+str(rc))
    client.subscribe("AreaExplorer")
    # connection_check()

def on_message(client, userdata, msg):
    message = (str(msg.payload))[2:-1]
    print(message)

    if "speedtest" in message: 
        print("→ Wifi test request received")
        client.publish(topic="AreaExplorer", payload=str(wifitest()))

    if "drive" in message:
        print("→ Drive request received")

    if "carbon_monoxide_measurement" in message:
        print("→ Carbon Monoxide measurement request received")
        client.publish(topic="AreaExplorer", payload=str(carbon_monoxide_measurement()))

    if "methane_measurement" in message:
        print("→ Methane measurement request received")
        client.publish(topic="AreaExplorer", payload=str(methane_measurement()))

    #blink_led()

async def connection_check():
    while 1:
        print("↻ Callback")
        time.sleep(2)
    

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message 

client.connect("test.mosquitto.org", 1883, 60)
client.loop_forever()



