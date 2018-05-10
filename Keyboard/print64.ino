void print64(uint64_t myByte) {
  Serial.println("");
  for (uint64_t mask = 0x8000000000000000; mask; mask >>= 1) {
    if (mask  & myByte)
      Serial.print('1');
    else
      Serial.print('0');
  }
  Serial.println("");
}
