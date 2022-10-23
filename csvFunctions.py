import csv
import os
import data
from datetime import datetime
import time

data.values()

def removeCSV():
	dat = os.listdir('csvfiles/')
	fileDate = '' #r = raw string
	for d in dat:
		currentDate = datetime.now().strftime("%d-%m-%Y")
		modTimesinceEpoc = os.path.getmtime('csvfiles/{0}'.format(d))
# Convert seconds since epoch to readable timestamp
		fileDate= time.strftime('%d-%m-%Y', time.localtime(modTimesinceEpoc))
		currentDateFormatted = datetime.strptime(currentDate,"%d-%m-%Y")
		fileDateformatted = datetime.strptime(fileDate,"%d-%m-%Y")
		difference = fileDateformatted.date() - currentDateFormatted.date()
		if(difference.days >= 10):
			print("Difference {0}".format(difference.days))
			os.remove('csvfiles/{0}'.format(d))

def doesCSVfileexists(fileName):
	dat = os.listdir('csvfiles/') #r = raw string
	exists = False
	jobCard = fileName.split('_')
	filetoFind = fileName
	for d in dat:
		jcfiletoFind = d.split('_')
		if(jcfiletoFind[0] == 'Send'):
		    if(jobCard[1] == jcfiletoFind[1]):
			    print(jcfiletoFind[1])
			    exists = True
		elif(jobCard[0] == jcfiletoFind[0]):
			print(jcfiletoFind[0])
			exists = True
		else:
			pass
	return exists

def createCSV(fileName):
	with open(fileName
	, 'wb') as csvfile:
		csvwriter = csv.writer(csvfile)
		
def addDatatoCSV():
	with open('csvfiles/{0}_time.csv'.
	format(data.jc)
	, 'a') as csvfile:
		csvwriter = csv.writer(csvfile)
		csvwriter.writerow([data.shotsCount,False])

def saveAfterSend(data,filename):
	with open('csvfiles/{0}'.format(filename),'a') as f:
	    writer = csv.writer(f)
	    writer.writerow(data)
	    print("data added")

def readDatafromCSV(filename):
	with open('csvfiles/{0}'. 
	format(filename)) as f:
	    reader = csv.reader(f)
	    return list(reader)

def getLatestDatafromCSV(filename):
	with open('csvfiles/{0}'. 
	format(filename)) as f:
	    reader = csv.reader(f)
	    return list(reader)
