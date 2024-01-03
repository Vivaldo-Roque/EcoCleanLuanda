#include <DHT_U.h>
#include <dht.h>
#include <DHT12.h>
#include <DHTesp.h>
#include <DHT.h>
#include <Ultrasonic.h> // Inclua a biblioteca Ultrasonic

#include <Arduino.h>

#include <WiFi.h>
#include <WiFiMulti.h>
#include <WiFiClientSecure.h>

#include <WebSocketsClient.h>

#include <ArduinoJson.h>

WiFiMulti WiFiMulti;
WebSocketsClient webSocket;

// Substitua com as informações da sua rede Wi-Fi
const char* ssid = "Vivaldo Roque";
const char* password = "VROQUE2024";

String serverAddress = "192.168.193.66";
int port = 80;

String idContentor = "f2ab21cb-fb3b-4ec4-8b0f-1910fb50847d";

// Configuração do sensor DHT11
#define DHTPIN 27    // Pino de dados do sensor DHT11
#define DHTTYPE DHT11   // Tipo do sensor DHT (DHT11)
DHT dht(DHTPIN, DHTTYPE);

// Pino do sensor de chuva
#define RAIN_SENSOR_PIN 13 // Pino do sensor de chuva

// Configuração do sensor ultrassônico
#define TRIGGER_PIN 14 // Pino de trigger do sensor ultrassônico
#define ECHO_PIN 35    // Pino de eco do sensor ultrassônico
Ultrasonic ultrasonic(TRIGGER_PIN, ECHO_PIN); // Cria uma instância do sensor ultrassônico

DynamicJsonDocument doc(1024);

String output = "";

void hexdump(const void *mem, uint32_t len, uint8_t cols = 16) {
  const uint8_t* src = (const uint8_t*) mem;
  Serial.printf("\n[HEXDUMP] Address: 0x%08X len: 0x%X (%d)", (ptrdiff_t)src, len, len);
  for(uint32_t i = 0; i < len; i++) {
    if(i % cols == 0) {
      Serial.printf("\n[0x%08X] 0x%08X: ", (ptrdiff_t)src, i);
    }
    Serial.printf("%02X ", *src);
    src++;
  }
  Serial.printf("\n");
}

String readSensors() {
  // Leitura dos sensores
  float temperature = dht.readTemperature();
  float humidity = dht.readHumidity();

  float distance = ultrasonic.read(); // Leitura da distância do sensor ultrassônico
  bool isRaining = digitalRead(RAIN_SENSOR_PIN);

  // Exibir os dados no monitor serial
  Serial.print("Temperature: ");
  Serial.print(temperature);
  Serial.println(" °C");
  Serial.print("Humidity: ");
  Serial.print(humidity);
  Serial.println(" %");
  Serial.print("Distance: ");
  Serial.print(distance);
  Serial.println(" cm");
  Serial.print("Is Raining: ");
  Serial.println(isRaining ? "Yes" : "No");

  delay(2000);

  char output[128];

  doc["sensor_temperatura"] = float(temperature);
  doc["sensor_umidade"] = float(humidity);
  doc["sensor_distancia"] = float(distance);
  doc["sensor_chuva"] = bool(isRaining);

  serializeJson(doc, output);

  return output;
}

void webSocketEvent(WStype_t type, uint8_t * payload, size_t length) {

  switch(type) {
    case WStype_DISCONNECTED:
      Serial.printf("[WSc] Disconnected!\n");
      break;
    case WStype_CONNECTED:
      Serial.printf("[WSc] Connected to url: %s\n", payload);
      // send message to server
      // webSocket.sendTXT(output);
      break;
    case WStype_TEXT:
      Serial.printf("[WSc] get text: %s\n", payload);
      delay(1000); // Tempo para enviar a resposta
      output = readSensors();
      // send message to server
      webSocket.sendTXT(output);
      break;
    case WStype_BIN:
      Serial.printf("[WSc] get binary length: %u\n", length);
      hexdump(payload, length);

      // send data to server
      // webSocket.sendBIN(payload, length);
      break;
    case WStype_ERROR:      
    case WStype_FRAGMENT_TEXT_START:
    case WStype_FRAGMENT_BIN_START:
    case WStype_FRAGMENT:
    case WStype_FRAGMENT_FIN:
      break;
  }

}

void setup() {
  // Serial.begin(921600);
  Serial.begin(115200);

  //Serial.setDebugOutput(true);
  Serial.setDebugOutput(true);

  Serial.println();
  Serial.println();
  Serial.println();

  for(uint8_t t = 4; t > 0; t--) {
    Serial.printf("[SETUP] BOOT WAIT %d...\n", t);
    Serial.flush();
    delay(1000);
  }

  // WiFiMulti.addAP(ssid, password);

  //WiFi.disconnect();
  // while(WiFiMulti.run() != WL_CONNECTED) {
  //  delay(100);
  // }

  // server address, port and URL
  // webSocket.begin(serverAddress, port, "/ws/contentor/" + idContentor + "/");

  // event handler
  // webSocket.onEvent(webSocketEvent);

  // use HTTP Basic Authorization this is optional remove if not needed
  // webSocket.setAuthorization("user", "Password");

  // try ever 5000 again if connection has failed
  // webSocket.setReconnectInterval(5000);

}

void loop() {
  // webSocket.loop();
  output = readSensors();  
}
