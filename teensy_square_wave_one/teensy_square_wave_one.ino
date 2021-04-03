// 参数用于计算帧率
double count = 0;   //计数器
double pre_count = 0;   //辅助计数器
double freq = 0;   //帧率
double microSec = 0;

// 获取幅值与串口通信
# define steps 300
# define minFreq 5000
# define freqStart 100000
int amplitude;   // 所获取的幅值不会为负数
int plot_tag = 1024;

void setup() {
  Serial.begin(9600);
  pinMode(4,OUTPUT);
}

void loop() {
  // 根据步进生成频率
  sendToPC(&plot_tag);
  for(int i = 1; i <= steps ; i++) {
    analogWriteFrequency(4, freqStart + i*minFreq);
    analogWrite(4, 128);                // 振幅，占空比50%，才能输出正弦波
    amplitude = analogRead(A0);
    sendToPC(&amplitude);
    // 在串口中显示数据
//    Serial.print(i);
//    Serial.print(" ");
//    Serial.println(amplitude);
  }
  // 计算fps
//   count++;    //count is only used in FPS()
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

// 1Mhz, 0.5V
// 2Mhz, 0.5V
// 5Mhz, 0.5V
// 10Mhz, 0.4V
