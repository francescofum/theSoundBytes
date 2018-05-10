
void printData(uint32_t timeArray[], uint32_t noteArray[], uint32_t statusArray[]) {
  for (uint16_t i = 0; i < 614; i++) {
    Serial.print(timeArray[i]);
    Serial.print("           ");
    Serial.print(noteArray[i]);
    Serial.print("           ");
    Serial.println(statusArray[i]);
  }
}

//*********************ISR PRINT STUFF************************
  //playnote(frequencies[*(pnoteArray+count)]);
  // Serial.print(frequencies[*(pnoteArray+count)]);
  // Serial.print("     ");
  // Serial.print(*(ptimeArray+count));
  // Serial.print("     ");
  // Serial.println(*(pstatusArray+count));
  //

//***********************************************************
