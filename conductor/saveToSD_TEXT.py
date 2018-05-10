
import os
from  midi2textv34 import *
import shutil

def downloadToSD(songName,pathToMidi,channel,pathToSD):
    
            
    midiFile = MIDI2TEXT(pathToMidi,str(channel))
    
    
    #check that the file path actually exists
    if (True):
        print('SD card found...Writing data.')
        #open the SD card directory and check is the song already exists
        os.chdir(pathToSD)
        for file in os.listdir():
            if(songName == file):
                pass
                #File already exists. Dont make duplicate file before proceeding
            else:
                #if file doesn't exist create it
                os.mkdir(str(songName))  
        #create three subfolders
        os.chdir(songName)
        #write all the timings
        print('Writing time data........',end=' ')
        fh_time = open('time.txt','w')
        fh_time.write(str(midiFile[0]))
        fh_time.close()
  
        print('Timings successfully written.')
        #write the status
        print('Writing note status......',end=' ')
        fh_status = open('status.txt','w')
        fh_status.write(str(midiFile[1]))
        fh_status.close()

        
        print('Status successfully written.')
        #write the notes
        print('Writing notes............',end=' ')
        fh_note = open('notes.txt','w')
        fh_note.write(str(midiFile[2]))
        fh_note.close()
        print('Notes successfully written.')

      
        print('''Files have been successfully downloaded to SD card.
Remove SD card safely to avoid data corruption''')       
        
    else:
        print('No SD card found, check that SD card has been mounted properly.')


