import pywifi
from pywifi import const

wifi = pywifi.PyWiFi()
iface = wifi.interfaces()[0]  # Assuming you have only one Wi-Fi interface, you can change this if needed.

print(iface.name)

