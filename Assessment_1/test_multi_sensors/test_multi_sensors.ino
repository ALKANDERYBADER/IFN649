/* 
 * IFN649_22_sem2
 * Bader ALKANDERY
 * N9334963
 * collect data from DHT and moisture sensor 
 * then send data via bluetooth to raspberry pi
 */
#include "DHT.h"
#include "TimeLib.h"
#define DHTPIN 21      // Digital pin connected to the DHT sensor
#define DHTTYPE DHT11   // DHT 11
DHT dht(DHTPIN, DHTTYPE);
#define rxPin 7 // Teensy pin 7 
#define txPin 8 // Teensy pin 8 

const int LEDPIN = 11;  // teensy LED
const int soilPin = 12; // soil sensor

void setup() {
  // Setup DHT Sensor
  pinMode(DHTPIN, INPUT);
  dht.begin();
  // Setup Serial1 for BlueTooth
  Serial1.begin(9600); // Default communication rate of the Bluetooth module
}

void loop() {
    digitalWrite(LEDPIN, HIGH); //set LED ON
    TempSensor(); // get temperature sensor readings
    SoilSensor(); // get soil sensor readings
    digitalWrite(LEDPIN, LOW); //set LED off
    delay(5000); // delay
}

void SoilSensor(){ // -----------------------------Soil sensor reading
  // send to bluetooth
  Serial1.print(" Soil Moisture: ");
  Serial1.println(analogRead(soilPin));
}

void TempSensor(){ // -----------------------Temperature sensor reading
//Humidity reading
    float h = dht.readHumidity();
    Serial1.print(F(" Humidity: "));
    Serial1.print(h);
    Serial1.println("%");
//Temperature reading
    float t = dht.readTemperature();
    Serial1.print(F(" Temperature: "));
    Serial1.print(t);
    Serial1.println(F("C"));
//Heat index reading
    float hic = dht.computeHeatIndex(t, h, false);  
    Serial1.print(F(" Heat index: "));
    Serial1.print(hic);
    Serial1.println(F("C "));
}
