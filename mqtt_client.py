import paho.mqtt.client as mqtt
from blink_led import blink_led

def on_connect(client, userdata, flags, rc): 
    print("Connected with result code "+str(rc))
    client.subscribe("measurements")

def on_message(client, userdata, msg):
    print(msg.topic+" "+str(msg.payload))
    blink_led()

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message 

client.connect("test.mosquitto.org", 1883, 60)
client.loop_forever()



