void setup() {
Serial.begin(9600);
delay(2000);
Serial.println("Arduino ready to receive!");
Serial.println("Waiting for messages...");
Serial.println("----------------------------");
}

void loop() {
if (Serial.available() > 0) {
String message = Serial.readStringUntil('\n');
Serial.print("Received: ");
Serial.println(message);
Serial.println("----------------------------");
}
}
