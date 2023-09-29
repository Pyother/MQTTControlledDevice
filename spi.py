# -*- coding: utf-8 -*-

import spidev
import time

# Inicjalizacja interfejsu SPI
spi = spidev.SpiDev()
spi.open(0, 0)  # Otwarcie interfejsu SPI na CS0 (GPIO 8)

# Funkcja do odczytu danych z MCP3008
def read_adc(channel):
    adc = spi.xfer2([1, (8 + channel) << 4, 0])
    data = ((adc[1] & 3) << 8) + adc[2]
    return data

try:
    while True:
        # Odczyt danych z czujnika MQ-9 (podłączony do CH0)
        mq9_channel = 0
        mq9_data = read_adc(mq9_channel)
        
        # Wyświetlanie odczytów
        print("Odczyt z czujnika MQ-9: {}".format(mq9_data))
        
        # Poczekaj chwilę przed kolejnym odczytem
        time.sleep(1)

except KeyboardInterrupt:
    spi.close()

