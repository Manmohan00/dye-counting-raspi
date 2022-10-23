from Keypad import *
from lcd import *
import data
import time
import RPi.GPIO as GPIO
import time
from proxy import *
from csvFunctions import *
import server
import schedule

setUp()
time.sleep(4)

clear()
removeCSV()
L = [26,20,21,16]
C = [5,6,13,19]

workDone = False
csvExists = False

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

GPIO.setup(L[0], GPIO.OUT)
GPIO.setup(L[1], GPIO.OUT)
GPIO.setup(L[2], GPIO.OUT)
GPIO.setup(L[3], GPIO.OUT)
GPIO.setup(C[0], GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(C[1], GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(C[2], GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(C[3], GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

data.values()

buzzer = 12
GPIO.setup(buzzer, GPIO.OUT, initial=GPIO.LOW)

schedule.every(3).seconds.do(server.sendData)

data.wifiCheck = server.checkInternet()

while True:
        readLine(L[0],["1","2","3","A"])
        readLine(L[1],["4","5","6","B"])
        readLine(L[2],["7","8","9","C"])
        readLine(L[3],["*","0","#","D"])

        if(data.wifiCheck == False and data.nextButton == 0):
                noWifi()
                #GPIO.output(buzzer, GPIO.HIGH)
                #time.sleep(1)
                #GPIO.output(buzzer, GPIO.LOW)
                #time.sleep(0.5)

        if(data.nextButton == 0 and data.wifiCheck == True):
           initialtext()

        elif(data.nextButton == 1):
            onEdit()

        elif(data.nextButton == 2):
            onJC()

        elif(data.nextButton == 3):
            onCA()

        elif(data.nextButton == 4):
            onShots()

        elif(data.nextButton == 5):
            onSubmit()
        
        elif(data.nextButton == 6):
                if(server.checkInternet()):
                        schedule.run_pending()
                else:
                        print("No Wifi for Schedule")
                showProd() 
                       
                if(proxyData()):
                        workDone = proxyCalculation()
                elif(workDone):
                        data.nextButton = 7
                        clear()
                else:
                       pass
                        
        elif(data.nextButton == 7):
                if(server.checkInternet()):
                    schedule.run_pending()
                prodDone()
        else:
                pass
