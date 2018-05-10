'''Midi2Text Python Script
   written by: Francesco Fumagalli (francesco.fum@gmail.com)
   ROBOT ORCHESTRA MENG PROJECT 2017/2018
'''
#NOTES
# v2.5.2 works with mid files containing one tempo. Other than that works perfectly. Has been tested against Anvil Studio output
# http://automatetheboringstuff.com/chapter7/ Info on regular expressions and overall good book.

from mido import MidiFile
import mido
import re



'''TODO :
	1. use pprint to justify the data printed
	2. change the file code so that it doesnt overwrite existing file
'''


def MIDI2TEXT(pathToMidi,selectChannel):
        '''DESCRIPTION OF REGULAR EXPRESSION GROUPS 
    the script uses regular expressions to extract the data.
    The groups are as follows:
	    For control message
				Group 1: "tempo"+number
				Group 2: only number

	    For note message
				Group 1: "note_on" or "note_off"
				Group 2: only the on/off part
				Group 3: "channel"+value
				Group 4: only the channel vale
				Group 5: "note"+value
				Group 6: only the note value
				Group 7: "velocity"+value
				group 8: velocity
				Group 9: "time"+vale
				Group 10: time in delta time
				'''
        
        tempo_regex=re.compile('.*(tempo=(\d+).*(time=(\d+)))')    #match tempo , if tempo isnt found, midi specifies a defaul of 500000
        note_regex =  re.compile(r'''(note_(on|off))\s  #match note_on/off
                                     (channel=(\d+))\s   #match channel
                                     (note=(\d+))\s      #match note
                                     (velocity=(\d+))\s    #velocity
                                     (time=(\d+))        #match time
        ''',re.VERBOSE)#use VERBOSE to make it clearer

        #Dictionary to convert midi notes into sheet notation - 
        sheet_notes = {'0':'C','12':'C','24':'C','36':'C','48':'C','60':'C','72':'C','84':'C','96':'C','108':'C','120':'C',
                 '1':'C#','13':'C#','25':'C#','37':'C#','49':'C#','61':'C#','73':'C#','85':'C#','97':'C#','109':'C#','121':'C#',
                 '2':'D','14':'D','26':'D','38':'D','50':'D','62':'D','74':'D','86':'D','98':'D','110':'D','122':'D',
                 '3':'D#','15':'D#','27':'D#','39':'D#','51':'D#','63':'D#','75':'D#','87':'D#','99':'D#','111':'D#','123':'D#',
                 '4':'E','16':'E','28':'E','40':'E','52':'E','64':'E','76':'E','88':'E','100':'E','112':'E','124':'E',
                 '5':'F','17':'F','29':'F','41':'F','53':'F','65':'F','77':'F','89':'F','101':'F','113':'F','125':'F',
                 '6':'F#','18':'F#','30':'F#','42':'F#','54':'F#','66':'F#','78':'F#','90':'F#','102':'F#','114':'F#','126':'F#',
                 '7':'G','19':'G','31':'G','43':'G','55':'G','67':'G','79':'G','91':'G','103':'G','115':'G','127':'G',
                 '8':'G#','20':'G#','32':'G#','44':'G#','56':'G#','68':'G#','80':'G#','92':'G#','104':'G#','116':'G#',
                 '9':'A','21':'A','33':'A','45':'A','57':'A','69':'A','81':'A','93':'A','105':'A','117':'A',
                '10':'A#','22':'A#','34':'A#','46':'A#','58':'A#','70':'A#','82':'A#','94':'A#','106':'A#','118':'A#',
                '11':'B','23':'B','35':'B','47':'B','59':'B','71':'B','83':'B','95':'B','107':'B','119':'B'}

        #store the values in individual arrays
        tempo = []
        note_status=[]
        channel=[]
        notes = []
        velocity=[]   #not used currently
        time=[]
        #path to various midi files
        path = pathToMidi
        #path = r"C:\Users\franc\Documents\MEng Project\songs\Survivor_-_Eye_of_the_Tigerv2.mid"
        #path = r"C:\Users\franc\Documents\MEng Project\songs\GameofThrones_v2.mid" #path to midi file
        #path = r"C:\Users\franc\Documents\MEng Project\songs\testSongs\HappyBirthdayv1.mid"
        #path = r"C:\Users\franc\Documents\MEng Project\songs\testSongs\twinkletwinkle.mid"
        #path = r"C:\Users\franc\Documents\MEng Project\songs\testSongs\happybirthday_01.mid"
        #path = r"C:\Users\franc\Downloads\happy_birthday_new.mid"

        mid = MidiFile(path) #create mido object

       
        for i,track in enumerate(mid.tracks):                            #loop though all the tracks
                #print(('Track {}:{}').format(i,track.name))             #print track name and contents track 0 contains the instruments
                for msg in track:                                        #loop though all the messages
                        if tempo_regex.search(str(msg)):
                                t = tempo_regex.search(str(msg))         #match tempo
                                tempo.extend(([(t.group(2))]))             #add tempo to tempo list
                                
                                

                             
                                      
                        if note_regex.search(str(msg)):                  #match note data
                                if len(tempo)==0:
                                        tempo.append("500000");#default tempo 500000
                             
                                n = note_regex.search(str(msg))
                                note_status.extend([n.group(2)])         #match note status
                                channel.extend([n.group(4)])             #match channel
                                notes.extend([n.group(6)])               #match notes
                                velocity.extend([n.group(8)])            #match velocity 
                                time_converted_to_sec = int(mido.tick2second(int(n.group(10)), mid.ticks_per_beat, (int(tempo[0])))*1000000)
                                #time_in_sec = "{0:06d}".format(time_converted_to_sec)       #+ time_in_sec
                                time_in_sec=time_converted_to_sec
                                time.extend([time_in_sec])                #time in sec from previous message


                          
        for i in range(0,len(notes)):
                
            if velocity[i] == '0':
                note_status[i]='off'
                
        for i in range(0,len(notes)):
            if (len(notes[i]) == 2):
                notes[i] = '0'+notes[i]
                
        for i in range(0,len(notes)):
            if note_status[i] == 'on':
                    note_status[i] = 1
            if note_status[i] == 'off':
                    note_status[i] = 0
        
 
                    
                
##   
        
                
        #get the position of where channel 0/1/2 etc start and stop
        #this way we can split the above arrays (time/note_status/note/velocity) into individual channels
        #rather than having one massive arrray with everything. So we can then send individual channels to individual instruments
        channel_index =list()
        numOfChans = len(set(channel))
        
        for chan in range(0,numOfChans):
                channel_index.append(channel.index(str(chan)))
   
        
        #generate a master list, with X nested lists (one for each channel)
        # and each X nested list has 3 more nested lists for time/note status/note
        masterList = [ [ [] for i in range(3) ] for i in range(numOfChans)]
       
        '''
        masterList breakdown:
            masterList [channel]
                            [0=time]
                            [1=note statuts]
                            [2=note]
                            
'''
        
        for channel in range(0,4):
    
            if channel == 3: 
                masterList[channel][0].append(time[channel_index[channel]:])
                masterList[channel][1].append(note_status[channel_index[channel]:])
                masterList[channel][2].append(notes[channel_index[channel]:])
                
                continue
                    
            masterList[channel][0].append(time[channel_index[channel]:channel_index[channel+1]])
            masterList[channel][1].append(note_status[channel_index[channel]:channel_index[channel+1]])
            masterList[channel][2].append(notes[channel_index[channel]:channel_index[channel+1]])

        
                                          

                                          
                                
                                
        
        if selectChannel == '1':
            returnList = []
            returnList.extend((masterList[0][0]))
            returnList.extend((masterList[0][1]))
            returnList.extend((masterList[0][2]))
            
            
            
            return returnList

        if selectChannel == '2':
            returnList = []
            returnList.extend(masterList[1][0])
            returnList.extend(masterList[1][1])
            returnList.extend(masterList[1][2])
            return returnList

        if selectChannel == '3':
            returnList = []
            returnList.extend(masterList[2][0])
            returnList.extend(masterList[2][1])
            returnList.extend(masterList[2][2])
            return returnList
        
        if selectChannel == '4':
            returnList = []
            returnList.extend(masterList[3][0])
            returnList.extend(masterList[3][1])
            returnList.extend(masterList[3][2])
            return returnList
        else:
                return masterList
     
        
      







        



####################################################    E N D    O F    F U N C T I O N  ###################################################################
#################################################################################################################################################################################
#chan =1
#path = r"C:\Users\franc\Documents\MEng Project\songs\GameofThrones_v2.mid"
#path =  r"C:\Users\franc\Documents\MEng Project\songs\DespacitoV1.mid"
#path = r"C:\Users\franc\Documents\MEng Project\songs\Eye_of_the_Tigerv.mid"
##path = r"C:\Users\franc\Documents\MEng Project\songs\Red_Hot_Chili_Peppers_-_Californicationv3.mid"
##save = r"C:\Users\franc\Documents\MEng Project\Software\Midi2Text\testfFile\dump"
##
#MIDI2TEXT(path,'3');


