void printNotes ()
{
  Serial.print("Count: ");
  Serial.print(count);
  Serial.print("    ");
  Serial.print("Current note: ");
  Serial.print(pnoteArray[count] - 24);
  Serial.print("    ");
  Serial.print(pnoteArray[count]);
  Serial.print("    ");
  Serial.print("Current status: ");
  Serial.print(pstatusArray[count]);
  Serial.print("    ");
  Serial.print("Current time: ");
  Serial.println(ptimeArray[count]);
}
