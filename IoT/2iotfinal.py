import requests
import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
pin = 14
GPIO.setup(pin, GPIO.OUT)
url = 'http://demo2.bisa.ai:3030/status_lampu'
while True:
    result = requests.get(url).json()['status_lampu']
    if result == 'on':
        print("Lampu Nyala")
        GPIO.output(pin, GPIO.LOW)
    else:
        print("Lampu Mati")
        GPIO.output(pin, GPIO.HIGH)
    time.sleep(1)

