#include "Arduino.h"

void setup() {
    Serial.begin(9600);
    pinMode(10, OUTPUT);
}

void loop() {
    while (Serial.available()) {
        int LEDstate = Serial.parseInt();
        digitalWrite(10, LEDstate);
    }
}