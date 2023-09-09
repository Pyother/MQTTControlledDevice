import RPi.GPIO as GPIO
import time

def blink_led():
    GPIO_PIN = 17

    GPIO.setmode(GPIO.BCM)
    GPIO.setup(GPIO_PIN, GPIO.OUT)

    GPIO.output(GPIO_PIN, GPIO.HIGH)
    time.sleep(1)
    GPIO.output(GPIO_PIN, GPIO.LOW)

    GPIO.cleanup()

