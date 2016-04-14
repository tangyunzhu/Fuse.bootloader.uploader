import subprocess
import sys
from PySide import QtGui, QtCore
import time
import shlex
import os

DetectMcu   = ""
m328p   ="0x1e950f"
m32u4   ="0x1e9587"
m2560   ="0x1e9801"
m644p   ="0x1e960a"
m16u2   ="0x1e9489"

bootloader_328p          = '../firmware/optiboot_atmega328.hex'
bootloader_Micro32u4     = '../firmware/Micro-prod-firmware-2012-11-23.hex'
bootloader_xadow         = '../firmware/Seeeduino-Xadow.hex'
bootloader_lite          = '../firmware/Seeed_Lite_v1_0.hex'
bootloader_leonardo      = '../firmware/Caterina-Leonardo.hex'
bootloader_ArduinoYUN101 = '../firmware/Caterina2_ArduinoYun101.hex'
bootloader_GenuinoYUN101 = '../firmware/Caterina2_GenuinoYun101.hex'
bootloader_2560          = '../firmware/Mega2560-prod-firmware-2011-06-29.hex'
bootloader_Seeeduino16u2 = '../firmware/Seeeduino_16u2.hex'
bootloader_Arduino16u2   = '../firmware/Uno_16u2_.hex'
bootloader_Mega16u2      = '../firmware/Mega_16u2.hex'
bootloader_644p          = '../firmware/optiboot_GroveCape_644pa_16m.hex'
bootloader_ArduinoPro    = '../firmware/ATmegaBOOT_168_atmega328_pro_8MHz.hex'

class Example(QtGui.QWidget):
    
    def __init__(self):
        super(Example, self).__init__()
        
        self.initUI()
        
    def initUI(self):      

#------------------------------Atmega328p Part ---------------------------#
        position_y=10
        ArduinoButton = QtGui.QPushButton('Arduino uno', self)
#        ArduinoButton.setCheckable(True)
        ArduinoButton.move(10, position_y)
        ArduinoButton.clicked[bool].connect(self.ArduinoUnoWrite)
        
        position_y=position_y+40        
        ArduinoProButton = QtGui.QPushButton('328p_3V3_8M', self)
        ArduinoProButton.move(10, position_y)
        ArduinoProButton.clicked[bool].connect(self.ArduinoProWrite)   

#------------------------------Atmega32u4 Part ---------------------------#

        ArduinoMicro = QtGui.QPushButton('Micro', self)
        position_y=position_y+40
        ArduinoMicro.move(10, position_y)
        ArduinoMicro.clicked[bool].connect(self.ArduinoMicroWrite)
        
        ArduinoMicro = QtGui.QPushButton('leonardo', self)
        position_y=position_y+40
        ArduinoMicro.move(10, position_y)
        ArduinoMicro.clicked[bool].connect(self.leonardoWrite)
        
        xadowButton = QtGui.QPushButton('Xadow', self)
        position_y=position_y+40
        xadowButton.move(10, position_y)
        xadowButton.clicked[bool].connect(self.xadowWrite)
        
        LiteButton = QtGui.QPushButton('Lite', self)
        position_y=position_y+40
        LiteButton.move(10, position_y)
        LiteButton.clicked[bool].connect(self.LiteWrite)

        ArduinoYun101Button = QtGui.QPushButton('A_YUN101', self)
        position_y=position_y+40
        ArduinoYun101Button.move(10, position_y)
        ArduinoYun101Button.clicked[bool].connect(self.ArduinoYUN101Write)
        
        GenuinoYun101Button = QtGui.QPushButton('G_YUN101', self)
        position_y=position_y+40
        GenuinoYun101Button.move(10, position_y)
        GenuinoYun101Button.clicked[bool].connect(self.GenuinoYUN101Write)

#------------------------------Atmega2560 Part ---------------------------#

        position_y=position_y+40
        megaButton = QtGui.QPushButton('Mega2560', self)
        megaButton.move(10, position_y)
        megaButton.clicked[bool].connect(self.ArduinoMegaWrite)
        
#------------------------------Atmega16u2 Part ---------------------------#
        position_y=position_y+40        
        Seeeduino16u2 = QtGui.QPushButton('Seeed16u2', self)
        Seeeduino16u2.move(10, position_y)
        Seeeduino16u2.clicked[bool].connect(self.Seeeduino_16u2Write)

        position_y=position_y+40        
        Arduino16u2 = QtGui.QPushButton('Genuino16u2', self)
        Arduino16u2.move(10, position_y)
        Arduino16u2.clicked[bool].connect(self.Arduino_16u2Write)
        
        position_y=position_y+40        
        Mega2560_16u2 = QtGui.QPushButton('Mega16u2', self)
        Mega2560_16u2.move(10, position_y)
        Mega2560_16u2.clicked[bool].connect(self.Mega2560_16u2Write)

#------------------------------Atmega644p Part ---------------------------#
        position_y=position_y+40        
        m644pButton = QtGui.QPushButton('Atmega644p', self)
        m644pButton.move(10, position_y)
        m644pButton.clicked[bool].connect(self.Arduino644pWrite)

     

        position_y=position_y+155
        logClearButton =QtGui.QPushButton("LogClear",self)
        logClearButton.move(10,position_y)
        logClearButton.clicked[bool].connect(self.log_clear)

        position_y=position_y+30
        chipDetectButton =QtGui.QPushButton("Chip detect",self)
        chipDetectButton.move(10,position_y)
        chipDetectButton.clicked[bool].connect(self.chip_detect)
        
        position_y=position_y+30
        ReadFlashButton =QtGui.QPushButton("Read Flash",self)
        ReadFlashButton.move(10,position_y)
        ReadFlashButton.clicked[bool].connect(self.readFlash)
 
        position_y=position_y+30
        WriteFlashButton =QtGui.QPushButton("Write Flash",self)
        WriteFlashButton.move(10,position_y)
        WriteFlashButton.clicked[bool].connect(self.writeFlash)
        
        position_y=position_y+30
        eraseFlashButton =QtGui.QPushButton("Erase Flash",self)
        eraseFlashButton.move(10,position_y)
        eraseFlashButton.clicked[bool].connect(self.eraseFlash)

        self.logTestEdit = QtGui.QTextEdit(self)
        self.logTestEdit.setGeometry(QtCore.QRect(100, 10, 550, 750))
        self.logTestEdit.setObjectName("logTestEdit")
        
        self.hFuselabel = QtGui.QLabel(self)
        self.hFuselabel.setGeometry(QtCore.QRect(100, 720, 100, 20))
        self.hFuselabel.setObjectName("hFuse")       

        self.lFuselabel = QtGui.QLabel(self)
        self.lFuselabel.setGeometry(QtCore.QRect(250, 720, 100, 20))
        self.lFuselabel.setObjectName("lFuse")

        self.eFuselabel = QtGui.QLabel(self)
        self.eFuselabel.setGeometry(QtCore.QRect(400, 720, 100, 20))
        self.eFuselabel.setObjectName("eFuse")
        
        self.setGeometry(200, 100, 670, 800)
        self.setWindowTitle('Fuse and Bootloader uploader v5')
        self.show()

    def log(self, text):
        self.logTestEdit.append(text)      
        
    def log_clear(self):
        self.clearFuseShow()
        self.logTestEdit.clear()  

    def chip_detect(self):
        global DetectMcu
        child1=subprocess.Popen("../avrdude.exe -c avrispmkII -P usb -p m328p",stdout=subprocess.PIPE,stderr=subprocess.PIPE)
        out=child1.communicate()
        self.logTestEdit.append(out[1]) 
        print out
        if m328p in out[1]:
            DetectMcu="m328p"
            self.log("-->find Atmega328p")
            return '1'
        if m32u4 in out[1]:
            DetectMcu="m32u4"
            self.log("-->find Atmega32u4")
            return '2'
        if m2560 in out[1]:
            DetectMcu="M2560"
            self.log("-->find Atmega2560")
            return '3'
        if m644p in out[1]:
            DetectMcu="m644p"
            self.log("-->find Atmega644p")
            return '4'
        if m16u2 in out[1]:
            DetectMcu="m16u2"
            self.log("-->find Atmega16u2")
            return '5'
#------------------------------Read flash Part --------------------------#  
    def readFlash(self):
        self.log("Reading, please wait....")
        if DetectMcu is "":
            self.log("-->Please detect chip first")
        else:
            cmd="../avrdude -c avrispmkII -P usb -p %s -U flash:r:downlaodflash.hex:i" %DetectMcu 
            child1=subprocess.Popen(cmd,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
            out=child1.communicate()
            self.log(out[0])
            self.log(out[1])
            self.log("-----------------------------------------------------------------------")
            self.log("")
            self.log("-->the flash content has been readed and save in this folder")
            self.log("")
            self.log("-----------------------------------------------------------------------")
            cmd="../avrdude -c avrispmkII -p %s -U lfuse:r:-:h -U hfuse:r:-:h -U efuse:r:-:h" %DetectMcu
            child1=subprocess.Popen(cmd,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
            out=child1.communicate()            
            lfuse=out[0][0:6]
            hfuse=out[0][6:11]
            efuse=out[0][11:16]
            strhfuse="High Fuse:"+hfuse.strip('\n')
            strlfuse="Low Fuse:"+lfuse.strip('\n')
            strefuse="Extend Fuse:"+efuse.strip('\n')
            self.hFuselabel.setText(strhfuse)
            self.hFuselabel.setStyleSheet('color: red')
            self.lFuselabel.setText(strlfuse)
            self.lFuselabel.setStyleSheet('color: red')
            self.eFuselabel.setText(strefuse)
            self.eFuselabel.setStyleSheet('color: red')
#            self.log(out[0])
            self.log(out[1])

    def clearFuseShow(self):
            self.hFuselabel.setText("")
            self.lFuselabel.setText("")
            self.eFuselabel.setText("")
#------------------------------Write flash Part --------------------------#
    def writeFlash(self):
        self.clearFuseShow()
        curDir=os.getcwd()
        flashHexDir=curDir+"\downlaodflash.hex"
        print "Current dir is:"+flashHexDir
        DirExists=os.path.exists(flashHexDir)
        if DirExists is False:
            self.log("-->Please read flash firt, downlaodflash.hex is not exist!")
        else:
            if DetectMcu is "":
                self.log("-->Please detect chip first!")
            else:
                cmd = "../avrdude -c avrispmkII -P usb -p %s  -U flash:w:downlaodflash.hex" %DetectMcu
                child1=subprocess.Popen(cmd,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
                out=child1.communicate()
                self.log(out[0])
                self.log(out[1])
                print "Write flash completed!"
#------------------------------Erase flash Part --------------------------#  
    def eraseFlash(self):
        self.clearFuseShow()
        if DetectMcu is "":
            self.log("-->Please detect chip first")
        else:
            cmd="../avrdude -c avrispmkII -P usb -p %s -e" %DetectMcu 
            child1=subprocess.Popen(cmd,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
            out=child1.communicate()
            self.log(out[0])
            self.log(out[1])
            print "Erase flash completed!"
#------------------------------Atmega328p Part ---------------------------#    
    def ArduinoUnoWrite(self):
        self.clearFuseShow()
        chip_number=self.chip_detect()
        if chip_number is '1':
            self.log("-->begin to write fuse and bootloader to Arduino Uno")
            cmd = "../avrdude -c avrispmkII -P usb -p m328p -U lfuse:w:0xFF:m -U hfuse:w:0xDA:m -U efuse:w:0x05:m -U flash:w:" + bootloader_328p
            child1=subprocess.Popen(cmd,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
            out=child1.communicate()
            self.log(out[0])
            self.log(out[1])
        else:
            self.log('-->Wrong chip model')
            
    def ArduinoProWrite(self):
        self.clearFuseShow()
        chip_number=self.chip_detect()
        if chip_number is '1':
            self.log("-->begin to write fuse and bootloader to Arduino Pro or Mini")
            cmd = "../avrdude -c avrispmkII -P usb -p m328p -U lfuse:w:0xFF:m -U hfuse:w:0xDA:m -U efuse:w:0x05:m -U flash:w:" + bootloader_ArduinoPro
            child1=subprocess.Popen(cmd,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
            out=child1.communicate()
            self.log(out[0])
            self.log(out[1])
        else:
            self.log('-->Wrong chip model')

#------------------------------Atmega32u4 Part ---------------------------#  
    def ArduinoMicroWrite(self):
        self.clearFuseShow()
        chip_number=self.chip_detect()
        if chip_number is '2':
            self.log("-->begin to write fuse and bootloader to Arduino leonardo")
            cmd = "../avrdude -c avrispmkII -P usb -p m32u4 -e -u -U lfuse:w:0xFF:m -U hfuse:w:0xD8:m -U efuse:w:0xCB:m -U flash:w:" + bootloader_Micro32u4
            child1=subprocess.Popen(cmd,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
            out=child1.communicate()
            self.log(out[0])
            self.log(out[1])
        else:
            self.log('-->Wrong chip model')

    def leonardoWrite(self):
        self.clearFuseShow()
        chip_number=self.chip_detect()
        if chip_number is '2':
            self.log("-->begin to write fuse and bootloader to Arduino leonardo")
            cmd = "../avrdude -c avrispmkII -P usb -p m32u4 -e -u -U lfuse:w:0xFF:m -U hfuse:w:0xD8:m -U efuse:w:0xCB:m -U flash:w:" + bootloader_leonardo
            child1=subprocess.Popen(cmd,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
            out=child1.communicate()
            self.log(out[0])
            self.log(out[1])
        else:
            self.log('-->Wrong chip model')

    def xadowWrite(self):
        self.clearFuseShow()
        chip_number=self.chip_detect()
        if chip_number is '2':
            self.log("-->begin to write fuse and bootloader to xadow")
            cmd = "../avrdude -c avrispmkII -P usb -p m32u4 -e -u -U lfuse:w:0xFF:m -U hfuse:w:0xD8:m -U efuse:w:0xCe:m -U flash:w:" + bootloader_xadow
            child1=subprocess.Popen(cmd,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
            out=child1.communicate()
            self.log(out[0])
            self.log(out[1])
        else:
            self.log('-->Wrong chip model')

    def LiteWrite(self):
        self.clearFuseShow()
        chip_number=self.chip_detect()
        if chip_number is '2':
            self.log("-->begin to write fuse and bootloader to Seeeduino Lite")
            cmd = "../avrdude -c avrispmkII -P usb -p m32u4 -e -u -U lfuse:w:0xFF:m -U hfuse:w:0xD8:m -U efuse:w:0xCe:m -U flash:w:" + bootloader_lite
            child1=subprocess.Popen(cmd,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
            out=child1.communicate()
            self.log(out[0])
            self.log(out[1])
        else:
            self.log('-->Wrong chip model')
    
    def ArduinoYUN101Write(self):
        self.clearFuseShow()
        chip_number=self.chip_detect()
        if chip_number is '2':
            self.log("-->begin to write fuse and bootloader to Arduino YUN 101")
            cmd = "../avrdude -c avrispmkII -P usb -p m32u4 -e -u -U lfuse:w:0xFF:m -U hfuse:w:0xD8:m -U efuse:w:0xCe:m -U flash:w:" + bootloader_ArduinoYUN101
            child1=subprocess.Popen(cmd,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
            out=child1.communicate()
            self.log(out[0])
            self.log(out[1])
        else:
            self.log('-->Wrong chip model')  
            
    def GenuinoYUN101Write(self):
        self.clearFuseShow()
        chip_number=self.chip_detect()
        if chip_number is '2':
            self.log("-->begin to write fuse and bootloader to Arduino YUN 101")
            cmd = "../avrdude -c avrispmkII -P usb -p m32u4 -e -u -U lfuse:w:0xFF:m -U hfuse:w:0xD8:m -U efuse:w:0xCe:m -U flash:w:" + bootloader_GenuinoYUN101
            child1=subprocess.Popen(cmd,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
            out=child1.communicate()
            self.log(out[0])
            self.log(out[1])
        else:
            self.log('-->Wrong chip model')        
#------------------------------Atmega2560 Part ---------------------------#  
    def ArduinoMegaWrite(self):
        self.clearFuseShow()
        chip_number=self.chip_detect()
        if chip_number is '3':
            self.log("-->begin to write fuse and bootloader to Arduino Mega")
            cmd = "../avrdude -c avrispmkII -P usb -p m2560 -e -u -U lfuse:w:0xFF:m -U hfuse:w:0xD8:m -U efuse:w:0xFD:m -U flash:w:" + bootloader_2560
            child1=subprocess.Popen(cmd,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
            out=child1.communicate()
            self.log(out[0])
            self.log(out[1])
        else:
            self.log('-->Wrong chip model')      

#------------------------------Atmega644p Part ---------------------------#  
    def Arduino644pWrite(self):
        self.clearFuseShow()
        chip_number=self.chip_detect()
        if chip_number is '4':
            self.log("-->begin to write fuse and bootloader to Aemega644p")
            cmd = "../avrdude -c avrispmkII -P usb -p m644p -e -u -U lfuse:w:0xFF:m -U hfuse:w:0xDE:m -U efuse:w:0xFD:m -U flash:w:" + bootloader_644p
            child1=subprocess.Popen(cmd,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
            out=child1.communicate()
            self.log(out[0])
            self.log(out[1])
        else:
            self.log('-->Wrong chip model')   

#------------------------------Atmega16u2 Part ---------------------------#    
    def Seeeduino_16u2Write(self):
        self.clearFuseShow()
        chip_number=self.chip_detect()
        if chip_number is '5':
            self.log("-->begin to write fuse and bootloader to Seeeduino's Atmega16u2")
            cmd = "../avrdude -c avrispmkII -P usb -p m16u2 -e -u -U lfuse:w:0xEF:m -U hfuse:w:0xD9:m -U efuse:w:0xF4:m -U flash:w:" + bootloader_Seeeduino16u2
            child1=subprocess.Popen(cmd,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
            out=child1.communicate()
            self.log(out[0])
            self.log(out[1])
        else:
            self.log('-->Wrong chip model')            

    def Arduino_16u2Write(self):
        self.clearFuseShow()
        chip_number=self.chip_detect()
        if chip_number is '5':
            self.log("-->begin to write fuse and bootloader to Arduino Uno's Atmega16u2")
            cmd = "../avrdude -c avrispmkII -P usb -p m16u2 -e -u -U lfuse:w:0xEF:m -U hfuse:w:0xD9:m -U efuse:w:0xF4:m -U flash:w:" + bootloader_Arduino16u2
            child1=subprocess.Popen(cmd,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
            out=child1.communicate()
            self.log(out[0])
            self.log(out[1])
        else:
            self.log('-->Wrong chip model')  

    def Mega2560_16u2Write(self):
        self.clearFuseShow()
        chip_number=self.chip_detect()
        if chip_number is '5':
            self.log("-->begin to write fuse and bootloader to Mega2560's Atmega16u2")
            cmd = "../avrdude -c avrispmkII -P usb -p m16u2 -e -u -U lfuse:w:0xEF:m -U hfuse:w:0xD9:m -U efuse:w:0xF4:m -U flash:w:" + bootloader_Mega16u2
            child1=subprocess.Popen(cmd,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
            out=child1.communicate()
            self.log(out[0])
            self.log(out[1])
        else:
            self.log('-->Wrong chip model')  
 
def main():
    
    app = QtGui.QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()

