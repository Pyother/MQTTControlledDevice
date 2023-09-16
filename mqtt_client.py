import paho.mqtt.client as mqtt
from blink_led import blink_led
from speedtest import speedtest

def on_connect(client, userdata, flags, rc): 
    print("Connected with result code "+str(rc))
    client.subscribe("measurements")

def on_message(client, userdata, msg):
    message = (str(msg.payload))[2:-1]
    print("On topic "+msg.topic+" received: "+message)
    
    blink_led()
    if message == "speedtest":
        speedtest()

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message 

client.connect("test.mosquitto.org", 1883, 60)
client.loop_forever()



