import RPi.GPIO as GPIO'
GPIO.setmode(GPIO.BCM)
pin = 14
GPIO.setup(pin, GPIO.OUT)
# Menyalakan
# GPIO.output(pin, GPIO.LOW)
#Mematikan
# GPIO.output(pin, GPIO.HIGN)