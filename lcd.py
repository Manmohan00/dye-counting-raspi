import RPi_I2C_driver
import time
import data

mylcd = RPi_I2C_driver.lcd()

mylcd.backlight(1)
mylcd.lcd_clear()
time.sleep(1)

data.values()

def setUp():
    mylcd.lcd_display_string('Initializing...',1)

def noWifi():
    #mylcd.lcd_display_string(server.checkInternet(),1)
    mylcd.lcd_display_string('No Wifi',1)
    mylcd.lcd_display_string('C-Try Again',2)
    mylcd.lcd_display_string('D-Continue',3)
    mylcd.lcd_display_string('without Wifi',4)

def initialtext():
    mylcd.lcd_display_string('MNo-00',1)
    mylcd.lcd_display_string_pos('JCNo-00',2,0)
    mylcd.lcd_display_string_pos('CAV-00',2,8)
    mylcd.lcd_display_string('Shots-00',3)
    mylcd.lcd_display_string('*-EDIT',4)
    
def onEdit():
    mylcd.lcd_display_string_pos('MNo-',1,0) #Machine Number
    mylcd.lcd_display_string_pos(data.machine,1,4)
    mylcd.lcd_display_string('B-Back C-Clear',3)
    mylcd.lcd_display_string('*-NEXT #-Submit',4)
    
def onJC():
    mylcd.lcd_display_string_pos('JCNo-',1,0) #Machine Number
    mylcd.lcd_display_string_pos(data.jc,1,5)
    mylcd.lcd_display_string('B-Back C-Clear',3)
    mylcd.lcd_display_string('*-NEXT #-Submit',4)
    
def onCA():
    mylcd.lcd_display_string_pos('Cavity-',1,0) #Machine Number
    mylcd.lcd_display_string_pos(data.ca,1,8)
    mylcd.lcd_display_string('B-Back C-Clear',3)
    mylcd.lcd_display_string('*-NEXT #-Submit',4)
    
def onShots():
    mylcd.lcd_display_string_pos('shots-',1,0) #Machine Number
    mylcd.lcd_display_string_pos(data.shots,1,7)
    mylcd.lcd_display_string('B-Back C-Clear',3)
    mylcd.lcd_display_string_pos('#-Submit',4,4)
    
def onSubmit():
    mylcd.lcd_display_string('MNo-{0}'.format(data.machine) ,1)
    mylcd.lcd_display_string_pos('JCNo-{0}'.format(data.jc),2,7)
    mylcd.lcd_display_string('CAV-{0}'.format(data.ca),2)
    mylcd.lcd_display_string('Shots-{0}'.format(data.shots),3)
    mylcd.lcd_display_string('B-Back #-Start',4)
    
def showProd():
    mylcd.lcd_display_string('MNo-{0}'.format(data.machine) ,1)
    mylcd.lcd_display_string_pos('JCNo-{0}'.format(data.jc),2,7)
    mylcd.lcd_display_string('CAV-{0}'.format(data.ca),2)
    mylcd.lcd_display_string('Shots-{0}'.format(data.shotsCount),3)
    mylcd.lcd_display_string('Prod-{0}'.format(data.prodCount),4)
    mylcd.lcd_display_string_pos('*-Stop',4,10)
    
def prodDone():
    mylcd.lcd_display_string('JCNo-{0}'.format(data.jc),1)
    mylcd.lcd_display_string('Prod-{0}'.format(data.prodCount) ,2)
    #mylcd.lcd_display_string('CAV-{0}'.format(data.ca),2)
    mylcd.lcd_display_string('Shots-{0}'.format(data.shotsCount),3)
    #mylcd.lcd_display_string('Prod-{0}'.format(data.prodCount),4)
    mylcd.lcd_display_string('*-Start New',4)
    
def clear():
    mylcd.lcd_clear()
