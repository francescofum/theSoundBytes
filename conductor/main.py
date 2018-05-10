


#pyqt imports
import sys
from PyQt4 import QtGui
from orchestraGUIv4 import Ui_Dialog
from PyQt4.Qt import QFileDialog
from fileinput import filename
#my imports
import os
import shelve
import os
import struct
import saveToSD_BINARY
import saveToSD_TEXT
import conductor
import time

    
#TODO: add song options as a list?!

class Main(QtGui.QDialog):
print(1)
    def SongSelection(self):
        print("select song")
        os.chdir(pathToMain)
        shelfFile = shelve.open('GUIconfig')  
        __SONGS_temp_ = shelfFile['__SONGS__']
        try:
            settings[6] = __SONGS_temp_[self.ui.SelectSong.currentText()]
        except Exception:
            pass
        shelfFile.close()

        
    def btnCardLocation_Clicked(self):
        try:
            savePath = str(QFileDialog.getSaveFileName(self,"Save as"))
            tempPath =savePath
        
            if len(savePath)>8: #teensy requires names of less than 8 characters
                savePath = os.path.join(os.path.dirname(savePath),os.path.basename(savePath)[:8])    
            __SONGS_temp_={os.path.basename(tempPath):os.path.basename(savePath)}
            settings[0] = savePath
            if not os.path.exists(settings[0]):
                os.makedirs(settings[0])      
            shelfFile = shelve.open('GUIconfig')
            if(not '__SONGS__' in shelfFile.keys()):
               shelfFile['__SONGS__'] = {}
               
            __SONGS_temp_2 =shelfFile['__SONGS__']
            
            if not list(__SONGS_temp_.keys())[0] in list(__SONGS_temp_2.keys()):
                __SONGS_temp_2.update(__SONGS_temp_)
                shelfFile['__SONGS__']=__SONGS_temp_2
                self.ui.SelectSong.addItems(list(__SONGS_temp_.keys()))
            else:
                pass
             #   print("key exists not adding")
            
            shelfFile.close()
            self.ui.lineEdit.setText(os.path.basename(tempPath))
        except Exception as e:
            pass
        
        
    
    def btnMIDILocation_Clicked(self):
        midiPath = QtGui.QFileDialog.getOpenFileName(self, 'Single File', "~/Desktop",'*.mid')
        if(os.path.exists(midiPath)):
            settings[1] = midiPath
        self.ui.lineEdit_2.setText(os.path.basename(midiPath))
        
    
    def btnUpload_Clicked(self):
        
        if (None in settings[0:4]):
            print(settings[0])
            print(settings[1])
            print(settings[2])
            print(settings[3])
            print("Make sure all the necessary fields are filled")
        else:
            print("Converting midi file...")
            if(settings[3] == 'binary'):
                print("to binary")
                saveToSD_BINARY.downloadToSD(settings[0],settings[1],settings[2],settings[0])
            if(settings[3] == 'text'):
                print("to text")
                saveToSD_TEXT.downloadToSD(settings[0],settings[1],settings[2],settings[0])
            pass
    
    def btnPlay_Clicked(self):
        if settings[6]  == None:
            settings[6] = self.ui.SelectSong.currentText()[0:8]
            
        if settings[5] == None:
            print("Select instrument")
        else:
            conductor.MQTT_publish("PLAY",track=settings[6],topic=settings[5])
            time.sleep(3)
            print("Transmitting START signal")
            conductor.MQTT_publish("START",topic=settings[5])
            
        
   
   
    def btnStop_Clicked(self):
        if(settings[5] == None):
            print("Make sure all the necessary fields are filled")
        else:
            conductor.MQTT_publish("STOP",topic=settings[5])
        pass
    
    
    def checkMidi_Checked(self):
        settings[4] = 1 #copy midi files
        pass
    


    def checkAll_Checked(self):
        settings[5] = -1
        pass
    
    def checkKeyboard_Checked(self):
        settings[5] = 2
        pass
    
    
    def checkStepper_Checked(self):
        settings[5] = 0
        pass
    
    
    def checkTesla_Checked(self):
        settings[5] = 3
        pass
    
    
    def checkXylophone_Checked(self):
        settings[5] = 1
        pass
    
    
    
    def FileType(self, index):
        if index == 0: ##binary
            settings[3] = 'binary'
            pass
        else:          ##text
            settings[3] = 'text'
            pass
    
    
    def selectInstrument(self, index):
        if index == 0:   #key
            settings[2] = 3
            pass
        elif index == 1: #xylo
            settings[2] = 2
            pass
        elif index == 2: #stepper
            settings[2] = 1
            pass
        else:            #tesla
            settings[2] = 4
            pass

    
    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        
        #SD Card Management        
        self.ui.btnCardLocation.clicked.connect(self.btnCardLocation_Clicked)
        self.ui.btnMIDILocation.clicked.connect(self.btnMIDILocation_Clicked)
        self.ui.btnUpload.clicked.connect(self.btnUpload_Clicked)
        self.ui.checkMIDI.toggled.connect(self.checkMidi_Checked)
        self.ui.tabFileType.activated.connect(self.FileType)
        self.ui.selectInstrument.activated.connect(self.selectInstrument)
        
        #Orchestra Settings
        self.ui.btnPlay.clicked.connect(self.btnPlay_Clicked)
        self.ui.btnStop.clicked.connect(self.btnStop_Clicked)
        self.ui.checKeyboard.toggled.connect(self.checkKeyboard_Checked)
        self.ui.checkStepper.toggled.connect(self.checkStepper_Checked)
        self.ui.checkTesla.toggled.connect(self.checkTesla_Checked)
        self.ui.checkXylophone.toggled.connect(self.checkXylophone_Checked)
        self.ui.checkAll.toggled.connect(self.checkAll_Checked)

        shelfFile = shelve.open('GUIconfig')     
        if(not '__SONGS__' in shelfFile.keys()):
           shelfFile['__SONGS__'] = {}
        __SONGS_temp_ =shelfFile['__SONGS__']
        shelfFile.close()
        self.ui.SelectSong.clear()
        self.ui.SelectSong.addItems(list(__SONGS_temp_.keys()))
                #executes when box is clicked
        self.ui.SelectSong.activated.connect(self.SongSelection)


if __name__ == '__main__':
    pathToMain = os.getcwd()
    os.chdir(pathToMain)
    print(pathToMain)
    conductor.MQTT_init()
    settings= [None,None,1,'binary',None,None,None] #MAKE GLOBAL
    app = QtGui.QApplication(sys.argv)
    window = Main()
    window.show()
    
    sys.exit(app.exec_())

##
##settings[0] = path to save
##settings[1] = path to midi
##settings[2] = select instrument (steppers default)
##settings[3] = binary
##settings[4] = copy midi
##settings[5] =
##settings[6] =
