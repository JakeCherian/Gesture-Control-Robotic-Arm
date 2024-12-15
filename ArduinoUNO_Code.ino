#include <Wire.h>
#include <Adafruit_PWMServoDriver.h>

Adafruit_PWMServoDriver srituhobby = Adafruit_PWMServoDriver();

#define servoMIN 150
#define servoMAX 600
#define servoCENTER ((servoMIN + servoMAX) / 2)

void setup() {
    Serial.begin(9600);
    srituhobby.begin();
    srituhobby.setPWMFreq(60);
}

void loop() {
    if (Serial.available() > 0) {
        String command = Serial.readStringUntil('\n'); // Read until newline
        command.trim(); // Remove any whitespace or newline characters

        if (command == "Right") {
            // Move base servo to the left
            srituhobby.setPWM(0, 0, servoMIN);
            Serial.println("Moving Left");
        } else if (command == "Left") {
            // Move base servo to the right
            srituhobby.setPWM(0, 0, servoMAX);
            Serial.println("Moving Right");
        } else if (command == "Center") {
            // Move base servo to the center
            srituhobby.setPWM(0, 0, servoCENTER);
            Serial.println("Centering");
        } else if (command == "Near") {
            // Move second servo forward (to a higher position)
            srituhobby.setPWM(1, 0, servoMAX);
            Serial.println("Moving Forward");
        } else if (command == "Far") {
            // Move second servo backward (to a lower position)
            srituhobby.setPWM(1, 0, servoMIN);
            Serial.println("Moving Backward");
        } else if (command == "Top") {
            // Run motor connected to 2nd port forward
            srituhobby.setPWM(2, 0, servoMAX);
            Serial.println("Motor 2 Moving Forward");
        } else if (command == "Bottom") {
            // Run motor connected to 2nd port backward
            srituhobby.setPWM(2, 0, servoMIN);
            Serial.println("Motor 2 Moving Backward");
        } else if (command == "Middle") {
            // Keep motor connected to 2nd port stationary
            srituhobby.setPWM(2, 0, servoCENTER);
            Serial.println("Motor 2 Stationary");
        }
        
        delay(100); // Short delay for stability
    }
}