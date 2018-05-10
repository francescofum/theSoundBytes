/*
   Steppers code V1.

   THIS SOFTWARE WORKS WITH TEENSY 3.5
   TO ADD YOUR INSTRUMENT EDIT void ISR() FUNCTION BELOW.
   DATA FROM THE SD CARD IS DOWNLOADED AUTOMATICALLY. THE DATA GIVEN TO THE USER IS THE FOLLOWING:
          - noteArray: AN ARRAY OF ALL THE NOTES IN THE SONG THAT NEED TO BE PLAYED, IN THE ORDER THAT THEY NEED TO BE PLAYED. USES MIDI NOTATION TO REPRESENT NOTES.
          - timeArray: AN ARRAY OF ALL THE NOTES IN THE SONG THAT NEED TO BE PLAYED, USES MIDI NOTATION
          - statusArray: AN ARRAY OF ALL 1s AND 0s, IF '1' PLAY THE NOTE IF '0' RELEASE THE NOTE.
   DON'T CHANGE ANY OF THE OTHER FUNCTIONS OTHER THAN void setup(), void loop(); AND void ISR()
   email: francesco.fum@gmail.com


*/

#include <SD.h>
#include <SparkFun_MiniGen.h>
#include <SPI.h>



//***** OBJECT DECLARATION *****//
File SDhandler;
IntervalTimer timer;
MiniGen gen(10);
//*****************************//
//****GLOBAL VARIABLES ********//
//for sd card
volatile uint32_t *ptimeArray; //time array pointer
volatile uint32_t *pnoteArray; //note array pointer
volatile uint32_t *pstatusArray; //status array pointer
volatile  uint16_t count = 0;
volatile int Size = 0;
//for MQTT
int ACTION;
String TRACK;
uint32_t timerz;

//SPECIFICALLY FOR STEPPER INSTRUMENT

//****************************//
uint64_t _time = 0; //DELETE IN FINAL VERSION
void setup() {
  //****SETUP FOR MQTT*********//
  pinMode(3, INPUT);
  delay(500);
  Serial.begin(115200);  //begin Serial to transmit to monitor.
  delay(500);
  Serial.println("Teensy starting...");
  Serial3.begin(115200); //begin Serial on pins 7(Rx) 8(Tx) used to comm. with esp
  delay(500);
  attachInterrupt(3, USARTavailable, RISING); //configure interrupt for usart.
  //****SETUP FOR OTHER HARDWARE *****//
  interrupts();//enable interrupts
  initSD();
  //driver_setup(); //no need, all setup is done in the hardware.
  gen.reset(); //reset dss to default state
  delay(1000);
  gen.setMode(MiniGen::SQUARE);  //square wave generator
  gen.setFreqAdjustMode(MiniGen::FULL); //look at minigen library for more info 
  //*******************************************************************************//
//  while(Serial3.available()){
//    Serial3.read();
//  }
}

void loop() {
/*
 * void loop is like a state machine, state 1 = play state 2 = stop and state 3 = list track (not implemented yet)
 */
  switch (ACTION) {
    case 1: //play case
      ACTION = 0;
      playTrack(TRACK);
      break;

    case 3: //list tracks casE
      ACTION = 0;
      listTracks();
      break;
  }

  /*******************************/
  /* this section can be used to control
     LEDs or other visual effects.
     Or to do anything else. however,when in play mode
     the code gets stuck in a while loop inside playTrack,
     so add any effects needed when the song is being played there.
  */
  /*****************************/
}
