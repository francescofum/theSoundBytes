
void listTracks(){
  SDhandler = SD.open("/");
  printDirectory(SDhandler, 0);
  Serial.println("done!");
 
}

void printDirectory(File dir, int numTabs) {
  while (true) {
    File entry =  dir.openNextFile();
    if (entry.isDirectory()) {
      Serial.println(entry.name());
      printDirectory(entry, numTabs + 1);
    }
    if (! entry) {
      // no more files
      break;
    }
    entry.close();
  }
}
