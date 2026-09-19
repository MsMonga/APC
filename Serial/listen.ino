// listen.ino — the Arduino end of the link.
// One message = one line. "1" turns the LED on, "0" turns it off.
// Anything else is not in the agreement, so it does nothing.

const int LED = 13;                 // the on-board LED — nothing to wire

void setup() {
  pinMode(LED, OUTPUT);
  Serial.begin(9600);               // the speed both sides agree on
  Serial.println("ready");          // one line, so the Pi knows we are here
}

void loop() {
  if (Serial.available() > 0) {
    String line = Serial.readStringUntil('\n');   // wait for the end of a line
    line.trim();                                  // drop the '\r' and spaces

    if (line == "1") {
      digitalWrite(LED, HIGH);
    } else if (line == "0") {
      digitalWrite(LED, LOW);
    }
    // No else. A message we were not told about does nothing.
  }
}
