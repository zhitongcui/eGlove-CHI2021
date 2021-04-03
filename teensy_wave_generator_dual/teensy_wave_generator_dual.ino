// Hardware Schematic
//                              10n
// PIN 9 --[10k]-+-----10mH---+--||-- OBJECT
//               |            |
//              3.3k          |
//               |            V 1N4148 diode
//              GND           |
//                            |
//Analog 2 ---+------+--------+
//            |      |
//          100pf   1MOmhm
//            |      |
//           GND    GND

// 参数用于计算帧率
double count = 0;       // 计数器
double pre_count = 0;   // 辅助计数器
double freq = 0;        // 帧率
double microSec = 0;

// 获取幅值与串口通信
# define steps 100
# define minFreq 5000
# define freqStart 100000
int amplitude_A;
int amplitude_B;
int plot_tag = 1024;  // 用于作标识符

void setup() {
  Serial.begin(38400);
  pinMode(5,OUTPUT);
  pinMode(4,OUTPUT);
}

void loop() {
  // 根据步进生成频率
  sendToPC(&plot_tag);
  for(int i = 1; i <= steps ; i++) {
    analogWriteFrequency(4, freqStart + i*minFreq);
    analogWrite(4, 128);  // 振幅，占空比50%，才能输出正弦波
    amplitude_A = analogRead(A0);
    delayMicroseconds(10);
    sendToPC(&amplitude_A); // 向串口发送数据

    // 在串口中显示数据
//    Serial.print(i);
//    Serial.print(" ");
//    Serial.println(amplitude_A);
  }
  for(int i = 1; i <= steps ; i++) {
    analogWriteFrequency(5, freqStart + i*minFreq);
    analogWrite(5, 128);  // 振幅，占空比50%，才能输出正弦波
    amplitude_B = analogRead(A5);
    delayMicroseconds(10);
    sendToPC(&amplitude_B); // 向串口发送数据

    // 在串口中显示数据
//    Serial.print(i);
//    Serial.print(" ");
//    Serial.println(amplitude_B);
  }
  // 计算fps
//   count++;    // count is only used in FPS()
//   FPS();
}

void FPS() {
  if(millis() % 1000 < 50) {
     freq = double((count-pre_count)*1000/(millis()-microSec));
     microSec = millis();
     pre_count = count;
     Serial.print("The fps is ");
     Serial.println(freq);
  }
}

void sendToPC(int* data) {
  byte* byteData = (byte*)(data);  // Casting to a byte pointer
  Serial.write(byteData, 2);       // Send through Serial to the PC
}

void sendToPC(double* data) {
  byte* byteData = (byte*)(data);
  Serial.write(byteData, 4);
}
