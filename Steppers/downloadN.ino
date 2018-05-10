
void downloadN(volatile uint32_t noteArray[], String track) {

  String Track = track + "/notes.dat";
  SDhandler = SD.open(Track.c_str());
  if (SDhandler) {
    uint16_t noteArraycounter = 0;
    while (SDhandler.available() > 0) {
      uint32_t note_ = 0;
      note_ = note_ | (SDhandler.read() << 24);
      note_ = note_ | (SDhandler.read() << 16);
      note_ = note_ | (SDhandler.read() << 8);
      note_ = note_ |  SDhandler.read();
      noteArray[noteArraycounter] = note_;
      noteArraycounter++;
    }
  }
  else {
    Serial.println("Failed to open file");
  }
  SDhandler.close();
}

