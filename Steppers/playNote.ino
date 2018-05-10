void playnote(float freq) {

  float frequency = freq;
  unsigned long freqReg = gen.freqCalc(frequency);
  gen.adjustFreq(MiniGen::FREQ0, freqReg);
}
