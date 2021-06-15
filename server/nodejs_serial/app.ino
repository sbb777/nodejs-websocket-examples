void setup() {
  // put your setup code here, to run once:
Serial.begin(115200);
}

void loop() {

if (Serial.available() > 0) {

Serial.println(" I got from node js : " + Serial.readString());
  

  }


}