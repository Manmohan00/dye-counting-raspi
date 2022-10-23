import requests
import data
import csv
from csvFunctions import *
import socket

data.values()

def checkInternet():
	IPaddress=socket.gethostbyname(socket.gethostname()+".local")
	if IPaddress.startswith("127.0"):
		#print(IPaddress)
		return False
	else:
		#print(IPaddress)
		#print("true")
		return True

def sendData():
	if(doesCSVfileexists('Send_{0}.csv'. 
	format(data.jc))):
		print("CSV exists")
		updates()
	else:
		if(data.jc == '0' and data.machine == '0' and 
		data.ca == '0' and data.shots == '0'):
			pass
		else:
			print("CSV created")
			createCSV('csvfiles/Send_{0}.csv'. 
			format(data.jc))
			updates()

def updates():
	listone = []
	listtwo = []
	
	listone = readDatafromCSV('{0}_time.csv'. 
	format(data.jc))

	listtwo = readDatafromCSV('Send_{0}.csv'. 
	format(data.jc))

	n = len(listtwo)

	url = 'http://208.109.12.216:86/home/Data'
	c = 0
	for l in listone:
		try:
			if(c != n):
				if(l[0] in listtwo[c]):
					#print("Match")
					c = c + 1   
			else:
				myobj = {
				'machineid': int(data.machine),
							'batchno' : int(data.jc),
							'block' : int(data.ca),
							'count' : int(l[0])
							}
				x = requests.post(url, data = myobj)
				print(x.text)
				if(x.ok):	
					saveAfterSend([l[0],True],'Send_{0}.csv'. 
					format(data.jc))
				else:
					print("check wifi")
		except IndexError:
			print("Done")
