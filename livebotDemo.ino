String message = "";
int ledPin = 13;

void setup() 
{ 
  Serial.begin(9600);
  pinMode(ledPin, OUTPUT);
}

void loop() 
{ 
  int i=0;
  char commandbuffer[100];

  if(Serial.available()){
     delay(100);
     while( Serial.available() && i< 99) {
        commandbuffer[i++] = Serial.read();
     }
     commandbuffer[i++]='\0';
  }

  if(i>0)
  {
    message = (char*)commandbuffer;
    message.toUpperCase();
  }
  
  if(message == "H" || message.indexOf("HIGH") >=0)
    digitalWrite(ledPin, HIGH);
  else if(message == "L" || message.indexOf("LOW") >=0)
    digitalWrite(ledPin, LOW);
}
