#include <DHT.h>
#include <DHT_U.h>
#include <dht.h>
#include <DHT12.h>
#include <DHTesp.h>
#include <dht.h>
#include <WiFi.h>
#include <HTTPClient.h>
#include <DHT.h>
#include <Ultrasonic.h> // Inclua a biblioteca Ultrasonic

// Substitua com as informações da sua rede Wi-Fi
const char* ssid = "elektron";
const char* password = "12345678";

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



void setup() {
  Serial.begin(115200);
  dht.begin();
  connectToWiFi();
}

void loop() {
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

  // Envio dos dados para a API
  sendSensorDataToAPI(temperature, humidity, distance, isRaining);

  // Aguarde antes de coletar e enviar dados novamente (por exemplo, a cada 5 minutos)
  delay(300000); // 5 minutos
}

void connectToWiFi() {
  Serial.print("Conectando ao Wi-Fi...");
  WiFi.begin(ssid, password);
  while (WiFi.status() != WL_CONNECTED) {
    delay(1000);
    Serial.print(".");
  }
  Serial.println("Conectado ao Wi-Fi.");
}

void sendSensorDataToAPI(float temperature, float humidity, float distance, bool isRaining) {
  // URL da sua API
  String apiURL = "http://example.com/api/update?temp=" + String(temperature) + "&humidity=" + String(humidity) + "&distance=" + String(distance) + "&rain=" + String(isRaining);

  HTTPClient http;
  http.begin(apiURL);

  int httpCode = http.GET();
  if (httpCode == HTTP_CODE_OK) {
    Serial.println("Dados enviados com sucesso para a API.");
  } else {
    Serial.print("Erro ao enviar dados para a API. Código de erro: ");
    Serial.println(httpCode);
  }

  http.end();
}
