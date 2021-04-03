#define steps 150
int tag = 1024;
int amp1, amp2;

void setup () {
  pinMode (9, OUTPUT);
  TCCR1A = 0;
  TCCR1B = 0;
  TCCR1A |= (1 << COM1A0);   // Toggle OC1A on Compare Match.
  TCCR1B |= (1 << WGM12);    // CTC mode
  Serial.begin(38400);
}

void loop () {

    sendToPC(&tag); // 设置标识符

    for (int i = 0; i < steps; i++) {
      TCCR1B &= 0xFE; // turns off timer
      TCNT1 = 0;      // resets timer counter register
      OCR1A = i;      // changes frequency step
      TCCR1B |= 0x01; // turns on timer
      amp1 = analogRead(0);
      delayMicroseconds(10);
      sendToPC(&amp1);
//      Serial.print(i,DEC);
//      Serial.print(" ");
//      Serial.println(analogRead(0), DEC);
    }
//    delayMicroseconds(10);
//    for (int i = 0; i < steps; i++) {
//      TCCR1B &= 0xFE; // turns off timer
//      TCNT1 = 0;      // resets timer counter register
//      OCR1A = i;      // changes frequency step
//      TCCR1B |= 0x01; // turns on timer
//      amp2 = analogRead(1);
//      delayMicroseconds(10);
//      sendToPC(&amp2);
////      Serial.print(i,DEC);
////      Serial.print(" ");
////      Serial.println(analogRead(1), DEC);
//    }
}

void sendToPC(int* data) {
  byte* byteData = (byte*)(data);
  Serial.write(byteData, 2);
}

void sendToPC(double* data) {
  byte* byteData = (byte*)(data);
  Serial.write(byteData, 4);
}
