void playTrack(String track) {

  Serial.print("Playing : ");
  Serial.println(track.c_str());

  getFileSize(track);
  SDhandler = SD.open(track.c_str()); //open GoT file

  if (SDhandler) {

    Serial.println("file opened successfully.");

    uint32_t *timeArray = (uint32_t*)malloc(sizeof(uint32_t) * Size);
    uint32_t *noteArray = (uint32_t*)malloc(sizeof(uint32_t) * Size);
    uint32_t *statusArray = (uint32_t*)malloc(sizeof(uint32_t) * Size);

    ptimeArray = timeArray;
    pnoteArray = noteArray;
    pstatusArray = statusArray;

    downloadT(timeArray, track);
    downloadN(noteArray, track);
    downloadS(statusArray, track);


    while(ACTION != 4){
      delay(50);
    }
   Serial.println("Starting..");   
    // printData(timeArray, noteArray, statusArray);
    timer.begin(ISR, 100);
    timer.update(timeArray[0]);
    
    while ((count < Size) && (ACTION != 2)) {
      //add visuals that will be active during song here
      delay(50);
    }

    //PUT STUFF HERE THAT NEEDS TO BE DONE AFTER THE SONG HAS FINISHED OR STOPPED.
    count = 0;
    timer.end();
    shiftIndex1 = 0;
    while (shiftIndex1 < 8) {
      shift1[shiftIndex1] = 0b00000000;
      //    print64(solenoidsCopy);
      //    print8(shift[shiftIndex]);
      digitalWrite(latchPin, 0);
      shiftOut(dataPin, clockPin, MSBFIRST, shift[shiftIndex]);
      digitalWrite(latchPin, 1);
      shiftIndex1 = shiftIndex1 + 1;
    }


    
    /*free up the memory allocted to timeArray,noteArray and statusArray.
      This needs to be done since we're allocatng memory dynamically.
      Memory is persistant and will remain unless freed,resulting in errors if a second song is played after
    */
    free(timeArray);
    free(noteArray);
    free(statusArray);

  }
  else {
    Serial.println("error opening file.");
  }

}

void getFileSize(String track) {
  String Track = track + "/size.dat";
  Serial.println("opening " + Track);//DELETE IN FINAL VERSION
  SDhandler = SD.open(Track.c_str());
  Size = 0 ;
  if (SDhandler) {

    Size = Size | (SDhandler.read() << 24);
    Size = Size | (SDhandler.read() << 16);
    Size = Size | (SDhandler.read() << 8);
    Size = Size |  SDhandler.read();

    Serial.println(Size);//DELETE IN FINAL VERSION
  }
  else {
    Serial.println("Error getting size");
  }
  SDhandler.close();
}


