/* *************************************************************
   Encoder driver function definitions - by James Nugen
   ************************************************************ */
   
   
#ifdef ARDUINO_ENC_COUNTER
  //below can be changed, but should be PORTD pins; 
  //otherwise additional changes in the code are required
  #define LEFT_ENC_PIN PB0  //pin 53 - B0
  #define RIGHT_ENC_PIN PK0  //pin A8 - K0
#endif
   
long readEncoder(int i);
void resetEncoder(int i);
void resetEncoders();

