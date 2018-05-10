void callback(char* topic, byte* payload, unsigned int length) {

  payload[length] = '\0'; //null terminate  char array
  MESSAGE = (char*)(payload);
  
  if (MESSAGE.startsWith("PLAY")) {
    Serial.print(MESSAGE); 
    //Serial.print(MESSAGE.substring(4));  
    digitalWrite(2, HIGH);
    client.publish(TOPIC_OUT, "1");
  } 
    else if (MESSAGE.startsWith("STOP")) {
    Serial.print("STOP");  
    digitalWrite(2, HIGH);
    client.publish(TOPIC_OUT, "1");
  }
  else if (MESSAGE.startsWith("listTracks")) {
    Serial.print("listTracks");
    digitalWrite(2, HIGH);
    client.publish(TOPIC_OUT, "1");
  }
  else if (MESSAGE.startsWith("START")) {
    Serial.print("START");
    digitalWrite(2, HIGH);
    client.publish(TOPIC_OUT, "1");
  }

  else {
    Serial.println("The request you made is unavailable. Try again.");
  }
  delay(100);
  digitalWrite(2, LOW);
}
