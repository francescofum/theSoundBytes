

#include <ESP8266WiFi.h>
#include <PubSubClient.h>

#define TOPIC_IN "TESLA_IN"  //Messages from Pi to tesla
#define TOPIC_OUT "TESLA_OUT" //messages from tesla to pi

#define MAX_MESSAGE_BUFF 400 //max buffer size before sending to arduino
WiFiClient ESPclient;
PubSubClient client(ESPclient);
String MESSAGE;
const char* ssid = "theSoundBytes";
const char* password = "TEAM11MENG";
const char* mqtt_server = "192.168.4.1";

void setup() {
  pinMode(2, OUTPUT);     // Initialize the BUILTIN_LED pin as an output
  digitalWrite(2, LOW);
  Serial.begin(115200);
  
  //while(!Serial);
  Serial.println("Starting");
  setup_wifi();
  client.setServer(mqtt_server, 1883);
  client.setCallback(callback);
}

void loop() {
  if (!client.connected()) {
    //  Serial.println("not conn");
    reconnect();
  }

  client.loop();
}
