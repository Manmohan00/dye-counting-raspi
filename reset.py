import data
import server

data.values

def resetVar():
    data.nextButton = 0
    data.machine = '0'
    data.jc = '0'
    data.ca = '0'
    data.prodCount = 0
    data.shots = '0'
    data.shotsCount = 0
    data.totalShots = 0
    data.wifiCheck = server.checkInternet()
