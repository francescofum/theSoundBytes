void ISR() {
  //Serial.println(count);
  //maybe declare frequencies as global? does it add computational time if they have to be decleard each time in the isr?
  float frequencies[] = {8.17, 8.66, 9.17, 9.72, 10.30, 10.91, 11.56, 12.24, 12.97, 13.75, 14.56, 15.43, //octave 1
                         16.35, 17.32, 18.35, 19.44, 20.60, 21.82, 23.12, 24.49, 25.95, 27.50, 29.13, 30.86, //octave 2
                         32.70, 34.64, 36.70, 38.89, 41.20, 43.65, 46.24, 48.99, 51.91, 55.00, 58.27, 61.73, //octave 3
                         65.40, 69.29, 73.41, 77.78, 82.40, 87.30, 92.49, 97.99, 103.82, 110.00, 116.54, 123.47, //octave 4
                         130.81, 138.59, 146.83, 155.56, 164.81, 174.61, 184.99, 195.99, 207.65, 220.00, 233.02, 246.94,// octave 5
                         261.62, 277.18, 293.66, 311.12, 329.62, 349.32, 369.99, 391.99, 415.90, 440.00, 466.16, 493.88, //octave 6
                         523.25, 554.36, 587.32, 622.25, 659.25, 698.45, 739.98, 783.99, 830.60, 880.00, 932.32, 987.76, //octave 7
                         1046.50, 1108.73, 1174.65, 1244.50, 1318.51, 1396.91, 1479.97, 1567.98, 1661.21, 1760.00, 1864.65, 1975.53, //octave 8
                         2093.00, 2217.46, 2349.31, 2489.01, 2637.02, 2793.82, 2959.95, 3135.96, 3322.43, 3520.00, 3729.31, 3951.06, //octave 9
                         4186.00, 4434.92, 4698.63, 4987.03, 5274.04, 5587.65, 5919.91, 6271.92, 6644.87, 7040.00, 7458.62, 7902.13, //octave 10
                         8372.01, 8869.84, 9397.27, 9956.06, 10548.08, 11175.30, 11839.82, 12543.85
                        };


  /*   HOW TO USE THE ISR:
      TO ACCESS AN ELEMENT IN THE THREE ARRAYS USE:
  *        *(pstatusArray + count)
  *        *(ptimeArray + count)
  *        *(pnoteArray + count)
            - THE VALUE OF COUNT IS SET TO ZERO INITIALLY. WHEN THE SONG REACHES THE END COUNT IS AUTOMATICALLY RESET TO 0, FOR A NEW SONG TO BE PLAYED
            - THE VALUE OF COUNT CORRESPONDS TO THE ELEMENT IN THE ARRAY THAT YOU WANT TO ACCESS.
              FOR EXAMPLE, IF YOU WANT TO ACCESS THE 5TH ELEMENT OF THE NOTE ARRAY YOU SHOULD WRITE:
  *                   *(pnoteArray + count) WHICH RETURNS THE VALUE IN THAT ELEMENT.
            -  TO UPDATE THE TIMER USE timer.update((*(ptimeArray + count)));
            -  IF YOU WANT TO SKIP THE NEXT TIME YOU WOULD USE: timer.update((*(ptimeArray + count + 1))); WHICH WOULD SKIP HE NEXT TIME NEXT TIME
            -  DON'T FORGET TO UPDATE THE COUNT, E.G COUNT++  AT THE END OF THE ISR TO MOVE TO THE NEXT SONG/NOTE/TIME ELEMENT
  */


  if (*(pstatusArray + count) == 1) { //check the status array if its 1 turn on the corresponding note
    playnote(frequencies[*(pnoteArray + count)]);
    
  }
  else {
    playnote(0); //turn off the corresponding note
  }
  count++;
  /*
     CHECK NEXT TIME
  */
  //check the next time element, if its equal to 0 perform that action as well
  if (*(ptimeArray + count) == 0) {
    do {
      if (*(pstatusArray + count) == 1) { //check the status array if its 1 turn on the corresponding note
        playnote(frequencies[*(pnoteArray + count)]);
      }
      else {
        //turn off the corresponding note
        playnote(0);
      }
      count++;
    } while (*(ptimeArray + count) == 0);
  }

  timer.update((*(ptimeArray + count)));
}
