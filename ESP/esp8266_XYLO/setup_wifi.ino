void setup_wifi() {

  delay(10);
  Serial.print("Connecting to ");
 Serial.println(ssid);
 WiFi.mode(WIFI_STA);
  WiFi.begin(ssid, password);
  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
   Serial.print(".");
  }
  digitalWrite(BUILTIN_LED, HIGH);
  Serial.println("");
  Serial.println("WiFi connected");
}


