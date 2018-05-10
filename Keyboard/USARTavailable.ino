/*
  ISR FOR READING AVAILABLE DATA FROM THE ESP MODULE.
  THIS ISR GETS CALLED WHEN GPIO2 OF THE ESP GOES HIGH.
  WHICH IT DOES ONLY WHEN IT HAS TRANSMITTED SOMETHING.
  READ THE INCOMING BYTES.
*/

void USARTavailable() {
 
  String MESSAGE;
  delay(5);
  toggle_led();
  Serial.print("Received from ESP: ");
  while (Serial3.available()>0) {
    MESSAGE = MESSAGE + (char) Serial3.read();
   //Serial.print(char(Serial3.read()));
  }
  Serial.println(MESSAGE);
  
  //Serial.print(MESSAGE);
  if (MESSAGE.startsWith("PLAY")) {
    ACTION = 1;
    TRACK = MESSAGE.substring(4);
  
  }
  else if (MESSAGE.startsWith("STOP")) {
    ACTION = 2;
    TRACK = "";
  }
  else if (MESSAGE.startsWith("listTrack")) {
    ACTION = 3;
    TRACK = "";
  }
  else if (MESSAGE.startsWith("START")){
    ACTION = 4;
    TRACK = "";
  }
//  Serial.print("MESSAGE: ");
//  Serial.println(MESSAGE);
//  Serial.print("TRACK: ");
//  Serial.println(TRACK);
 
}

void toggle_led(){
  if(digitalRead(13)==HIGH){digitalWrite(13,LOW);}
  else(digitalWrite(13,HIGH));
}

