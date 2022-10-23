import time
import RPi.GPIO as GPIO

buzzer = 12
GPIO.setmode(GPIO.BCM)
GPIO.setup(buzzer, GPIO.OUT, initial=GPIO.LOW)

while True:
	print("OK")
	GPIO.output(buzzer, GPIO.HIGH)
	time.sleep(1)
	GPIO.output(buzzer, GPIO.LOW)
	time.sleep(0.5)
