import RPi.GPIO as GPIO
import time
import data
from csvFunctions import addDatatoCSV

p = 4

GPIO.setmode(GPIO.BCM)
GPIO.setup(p,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)
data.values()

def proxyData():
	if GPIO.input(p) == 1:
   		return False
	else:
   		return True
	#time.sleep(0.5)

def proxyCalculation():
	if(data.shotsCount != data.totalShots):
		data.shotsCount = data.shotsCount + 1
		data.prodCount = data.shotsCount * int(data.ca)
		addDatatoCSV()
		
	else:
		return True
