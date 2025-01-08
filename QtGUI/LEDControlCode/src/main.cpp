#include "Arduino.h"

void setup() {
    Serial.begin(9600);
    pinMode(10, OUTPUT);
}

void loop() {
    while (Serial.available()) {
        int LEDstate = Serial.parseInt();
        digitalWrite(10, LEDstate);
        if (LEDstate == 1) {
            Serial.write("S1");
        } else {
            Serial.write("S0");
        }
    }
}