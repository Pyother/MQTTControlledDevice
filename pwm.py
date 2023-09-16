import RPi.GPIO as GPIO
import time

def pwm_led():
    GPIO_PIN = 13
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(GPIO_PIN, GPIO.OUT)
    p = GPIO.PWM(GPIO_PIN, 50)
    p.start(20)
    time.sleep(2)
    p.stop()
    GPIO.cleanup()

pwm_led()
