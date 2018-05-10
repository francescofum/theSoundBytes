
void downloadT(volatile uint32_t timeArray[], String track) {

  String Track = track + "/time.dat";
  
  SDhandler = SD.open(Track.c_str());
  if (SDhandler) {
    uint16_t timeArraycounter = 0;
    while (SDhandler.available() > 0) {
      uint32_t time_ = 0;
      time_ = time_ << (SDhandler.read() << 24);
      time_ = time_ | (SDhandler.read() << 16);
      time_ = time_ | (SDhandler.read() << 8);
      time_ = time_ |  SDhandler.read();
      timeArray[timeArraycounter] = time_;
      timeArraycounter++;
    }
  }
  else {
    Serial.println("Failed to open file.");
  }
  SDhandler.close();
}

