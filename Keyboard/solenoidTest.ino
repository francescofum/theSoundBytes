//void solenoidTest ()
//{
//  if ( trigger1 == 1) {
//    shift[0] = 0b00000001;
//    digitalWrite(latchPin, 0);
//    shiftOut(dataPin, clockPin, MSBFIRST, shift[0]);
//    digitalWrite(latchPin, 1);
//    trigger1 = 0;
//    count = count + 1;
//    Serial.println(count);
//    timer.update(ptimeArray[count]);
//  }
//  else {
//    shift[1] = 0b00000100;
//    digitalWrite(latchPin, 0);
//    shiftOut(dataPin, clockPin, MSBFIRST, shift[1]);
//    digitalWrite(latchPin, 1);
//    trigger1 = 1;
//    count = count + 1;
//    Serial.println(count);
//    timer.update(ptimeArray[count]);
//  }
//}
