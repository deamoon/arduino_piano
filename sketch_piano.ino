#define BUZZER_PIN 3

String message;

void setup() {
  pinMode(BUZZER_PIN, OUTPUT);
  Serial.begin(9600);
}

void loop() {
  static int frequency = 100;
  
  while (Serial.available()) {
    char inChar = Serial.read();
    if (inChar == '\n') {
      frequency = message.toInt();
      message = "";      
    } else {
      if (inChar >= '0' && inChar <= '9') {
        message += inChar;  
      }        
    }  
  }
  
  tone(BUZZER_PIN, frequency, 20);
}
