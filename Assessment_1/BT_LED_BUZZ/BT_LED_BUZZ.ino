/* 
 * IFN649_22_sem2
 * Bader ALKANDERY
 * N9334963
 * Receive CMD from Raspberry pi via bluetooth to switch on/off LED or Buzzer
 */
#define LED 13 // LED pin
#define BUZZ 12 // Buzzer pin

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  Serial1.begin(9600);
  pinMode(LED, OUTPUT); // Declare the LED as an output
  pinMode(BUZZ, OUTPUT);// Declare the BUZZ as an output
  }

void loop() {
  
  if(Serial1.available() > 0){
    String str = Serial1.readString();
    Serial.println(str);//check str on monitor
    if(str == "LED1"){
      digitalWrite(LED, HIGH); // Turn the LED on
    }else if(str =="LED0"){
      digitalWrite(LED, LOW); // Turn the LED OFF
    }else if(str == "BUZZ1"){
      digitalWrite(BUZZ, HIGH); // Turn the Buzz on
    }else if(str == "BUZZ0"){
      digitalWrite(BUZZ, LOW); // Turn the Buzz off
    }
  }
}
