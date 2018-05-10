
import os
from  midi2textv34 import *
import shutil
import struct

def downloadToSD(songName,pathToMidi,channel,pathToSD):
    

    midiFile = MIDI2TEXT(pathToMidi,str(channel))
    
    
    #check that the file path actually exists
    if (True):
        print('SD card found...Writing data.')
        #open the SD card directory and check is the song already exists
        os.chdir(pathToSD)
        for file in os.listdir():
            if(songName == file):
                print("File already exists. Delete file before proceeding.")
                return
        #if file doesn't exist create it
        if not os.path.exists(str(songName)):
            os.mkdir(str(songName))
        #create three subfolders
        os.chdir(songName)

        
        #write all the timings
        print('Writing time data........',end=' ')
        fh_time = open('time.dat','wb')
        #fh_time.write(int(midiFile[0]))
        for time in midiFile[0]:
           fh_time.write(struct.pack('>I',int(time)))
        fh_time.close()
        
        print('Timings successfully written.')

        
        #write the status
        print('Writing note status......',end=' ')
        fh_status = open('status.dat','wb')
        for status in midiFile[1]:
           fh_status.write(struct.pack('>I',int(status)))
        fh_status.close()
        print('Status successfully written.')

        
        #write the notes
        print('Writing notes............',end=' ')
        fh_note = open('notes.dat','wb')
        count = 0
        for note in midiFile[2]:
            fh_note.write(struct.pack('>I',int(note)))
        fh_note.close()
        print('Notes successfully written.')

        print("Writing size of arrays........",end=' ')
        fh_size = open('size.dat','wb')
        fh_size.write(struct.pack('>I',int(len(midiFile[2]))))
        fh_size.close()
        print(len(midiFile[2]))
        print('Length successfully written.')

      
        print('''Files have been successfully downloaded to SD card.
Remove SD card safely to avoid data corruption''')       
        
    else:
        print('No SD card found, check that SD card has been mounted properly.')







