import paho.mqtt.client as mqtt
from wifitest import wifitest
#from blink_led import blink_led

def on_connect(client, userdata, flags, rc): 
    print("Connected with result code "+str(rc))
    client.subscribe("AreaExplorer")

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

    if "methane_measurement" in message:
        print("→ Methane measurement request received")

    #blink_led()

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message 

client.connect("test.mosquitto.org", 1883, 60)
client.loop_forever()



