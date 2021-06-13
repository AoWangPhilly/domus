#include <DHT.h>
#include <DHT_U.h>

#define TYPE DHT11

int sensePin = 2;
DHT HT(sensePin, TYPE);

float humidity;
float tempC;
float tempF;

// delay a minute between each read
unsigned long setTime = 5*60*1000UL;

void setup() {
  Serial.begin(9600);
  HT.begin();
}

void loop() {
  humidity = HT.readHumidity();
  tempC = HT.readTemperature();

  if (!isnan(humidity) && !isnan(tempC)){
    Serial.print(humidity);
    Serial.print("\t");
    Serial.print(tempC);
    Serial.println();
  }
  delay(setTime);
}
