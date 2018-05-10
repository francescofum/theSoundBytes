
void downloadS(volatile uint32_t statusArray[], String track) {

  String Track = track + "/status.dat";
  SDhandler = SD.open(Track.c_str());
  if (SDhandler) {
    uint16_t statusArraycounter = 0;
    while (SDhandler.available() > 0) {
      uint32_t status_ = 0;
      status_ = status_ | (SDhandler.read() << 24);
      status_ = status_ | (SDhandler.read() << 16);
      status_ = status_ | (SDhandler.read() << 8);
      status_ = status_ |  SDhandler.read();
      statusArray[statusArraycounter] = status_;
      statusArraycounter++;
    }
 
  }


  else {
    Serial.println("Failed to open file");
  }
  SDhandler.close();
}

