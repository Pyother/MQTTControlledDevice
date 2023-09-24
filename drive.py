import RPi.GPIO as GPIO
import time

# Ustawienie pinów dla L298N
IN1 = 17
IN2 = 18
IN3 = 22
IN4 = 23

# Inicjalizacja GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(IN1, GPIO.OUT)
GPIO.setup(IN2, GPIO.OUT)
GPIO.setup(IN3, GPIO.OUT)
GPIO.setup(IN4, GPIO.OUT)

# Funkcja do przodu
def north():
    GPIO.output(IN1, GPIO.HIGH)
    GPIO.output(IN2, GPIO.LOW)
    GPIO.output(IN3, GPIO.HIGH)
    GPIO.output(IN4, GPIO.LOW)

# Funkcja do tyłu
def south():
    GPIO.output(IN1, GPIO.LOW)
    GPIO.output(IN2, GPIO.HIGH)
    GPIO.output(IN3, GPIO.LOW)
    GPIO.output(IN4, GPIO.HIGH)

# Funkcja do skrętu w lewo
def west():
    GPIO.output(IN1, GPIO.LOW)
    GPIO.output(IN2, GPIO.LOW)
    GPIO.output(IN3, GPIO.HIGH)
    GPIO.output(IN4, GPIO.LOW)

# Funkcja do skrętu w prawo
def east():
    GPIO.output(IN1, GPIO.HIGH)
    GPIO.output(IN2, GPIO.LOW)
    GPIO.output(IN3, GPIO.LOW)
    GPIO.output(IN4, GPIO.LOW)

# Funkcja do zatrzymania silników
def stop():
    GPIO.output(IN1, GPIO.LOW)
    GPIO.output(IN2, GPIO.LOW)
    GPIO.output(IN3, GPIO.LOW)
    GPIO.output(IN4, GPIO.LOW)

def drive():
    try:
        while True:
            # Testowanie ruchu silników
            north()
            time.sleep(2)

            south()
            time.sleep(2)

            west()
            time.sleep(2)

            east()
            time.sleep(2)

            stop()
            time.sleep(2)

    except KeyboardInterrupt:
        # Obsługa przerwania programu przez użytkownika (Ctrl+C)
        stop()
        GPIO.cleanup()

drive()