import RPi.GPIO as GPIO
import time
import data
from lcd import clear
from csvFunctions import *
from reset import *
import server

data.values()

L = [26,20,21,16]
C = [5,6,13,19]

def backSpace():
    if(data.nextButton == 1 and data.machine != '0'):
      clear()
      data.machine = data.machine[:-1]
    if(data.nextButton == 2 and data.jc != '0'):
      clear()
      data.jc = data.jc[:-1]
    if(data.nextButton == 3 and data.ca != '0'):
      clear()
      data.ca = data.ca[:-1]
    if(data.nextButton == 4 and data.shots != '0'):
      clear()
      data.shots = data.shots[:-1]

def readLine(line, characters):

    GPIO.output(line, GPIO.HIGH)

    if(GPIO.input(C[0]) == 1):
        if(characters[0] == "*"):
             if(data.nextButton < 4):
                clear()
                data.nextButton = data.nextButton + 1
             elif(data.nextButton == 6):
                clear()
                data.nextButton = 7
             elif(data.nextButton == 7):
                clear()
                resetVar()
                data.nextButton = 0
        if(data.nextButton == 1 and characters[0] != "*" ):
            if(data.machine == '0'):
                data.machine = characters[0]
            else:
                data.machine = data.machine + characters[0]
        if(data.nextButton == 2 and characters[0] != "*"):
            if(data.jc == '0'):
                data.jc = characters[0]
            else:
                data.jc = data.jc + characters[0]
        if(data.nextButton == 3 and characters[0] != "*" ):
            if(data.ca == '0'):
                data.ca = characters[0]
            else:
                data.ca = data.ca + characters[0]
        if(data.nextButton == 4 and characters[0] != "*" ):
            if(data.shots == '0'):
                data.shots = characters[0]
            else:
                data.shots = data.shots + characters[0]

    if(GPIO.input(C[1]) == 1):
        if(data.nextButton == 1 ):
            if(data.machine == '0'):
                data.machine = characters[1]
            else:
                data.machine = data.machine + characters[1]
        if(data.nextButton == 2):
             if(data.jc == '0'):
                    data.jc = characters[1]
             else:
                data.jc = data.jc + characters[1]
        if(data.nextButton == 3):
             if(data.ca == '0'):
                data.ca = characters[1]
             else:
                data.ca = data.ca + characters[1]
        if(data.nextButton == 4):
             if(data.shots == '0'):
                data.shots = characters[1]
             else:
                data.shots = data.shots + characters[1]

    if(GPIO.input(C[2]) == 1):
        if(characters[2] == "#"):
            clear()
            if(data.nextButton == 4):
              print(characters[2])
              filename = '{0}_time.csv'.format(data.jc)
              if(doesCSVfileexists(filename)):
                  last = getLatestDatafromCSV(filename)
                  lenght = len(last)
                  print(last)
                  try:
                         last = last[lenght-1][0]
                  except IndexError:
                         last = '0'
                  data.shotsCount = int(last)
                  print('shots - {0}'.format(last))
              data.nextButton = 5
            else:
              filename = '{0}_time.csv'.format(data.jc)
              if(doesCSVfileexists(filename)):
                  print("csv there")
                  data.totalShots = data.shotsCount + int(data.shots)
                  data.nextButton = 6
              else:
                  createCSV('csvfiles/{0}_time.csv'.format(data.jc))
                  print("csv not there")
                  data.totalShots = data.shotsCount + int(data.shots)
                  data.nextButton = 6
        if(data.nextButton == 1 and characters[2] != "#"):
             if(data.machine == '0'):
                data.machine = characters[2]
             else:
                data.machine = data.machine + characters[2]
        if(data.nextButton == 2 and characters[2] != "#"):
              if(data.jc == '0'):
                data.jc = characters[2]
              else:
                data.jc = data.jc + characters[2]
        if(data.nextButton == 3 and characters[2] != "#"):
              if(data.ca == '0'):
                data.ca = characters[2]
              else:
                data.ca = data.ca + characters[2]
        if(data.nextButton == 4 and characters[2] != "#"):
              if(data.shots == '0'):
                data.shots = characters[2]
              else:
                data.shots = data.shots + characters[2]

    if(GPIO.input(C[3]) == 1):
         if(characters[3] == "D" and data.nextButton == 0 and data.wifiCheck == False):
             data.wifiCheck = True
             clear()
         if(characters[3] == "C" and data.nextButton == 0 and data.wifiCheck == False):
             data.wifiCheck = server.checkInternet()
             clear()
         if(characters[3] == "B" and data.nextButton != 6 and data.nextButton != 0):
             clear()
             data.nextButton = data.nextButton - 1
         if(characters[3] == "C"):
             backSpace()
         if(data.nextButton == 1 and characters[3] != "B" and characters[3] != "C"):
             if(data.machine == '0'):
                 data.machine = characters[3]
             else:
                data.machine = data.machine + characters[3]
         if(data.nextButton == 2 and characters[3] != "B" and characters[3] != "C"):
             if(data.jc == '0'):
                 data.jc = characters[3]
             else:
                data.jc = data.jc + characters[3]
         if(data.nextButton == 4 and characters[3] != "B" and characters[3] != "C"):
             if(data.ca == '0'):
                 data.ca = characters[3]
             else:
                data.ca = data.shots + characters[3]
         if(data.nextButton == 3 and characters[3] != "B" and characters[3] != "C"):
             if(data.shots == '0'):
                 data.shots = characters[3]
             else:
                data.shots = data.ca + characters[3]

    GPIO.output(line, GPIO.LOW)

