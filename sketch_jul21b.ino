 const int buttonPin = 3;    
  const int ledPin =  13;      
  void setup() {
    pinMode(ledPin, OUTPUT);      
    pinMode(buttonPin, INPUT);
    Serial.begin(9600);     
  }
  void loop()
  {
    Serial.println(digitalRead(buttonPin));
    delay(20);
     if (digitalRead(buttonPin) == LOW) 
     {     
       digitalWrite(ledPin, HIGH);  
     } 
     else {
       digitalWrite(ledPin, LOW); 
     }
  }
