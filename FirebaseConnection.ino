#include <WiFi.h>
#include <Firebase_ESP_Client.h>
#include "addons/TokenHelper.h"
#include "addons/RTDBHelper.h"

#define WIFI_SSID "tester"
#define WIFI_PASSWORD "12345678"

#define API_KEY "AIzaSyAkDHhaqQsfGsW-byRXsikrq6YXMahBo5w"
#define DATABASE_URL "https://firebot-75055-default-rtdb.firebaseio.com/"

#define USER_EMAIL "kitreksu@gmail.com"
#define USER_PASSWORD "asd123*"

FirebaseData fbdo;
FirebaseAuth auth;
FirebaseConfig config;

unsigned long sendDataPrevMillis = 0;
bool signupOK = false;

#define LA 5
#define LB 18

#define RA 19
#define RB 21

int dataIn = 0;

void setup() 
{
  Serial.begin(9600);

  pinMode(LED_BUILTIN, OUTPUT);

  pinMode(LA, OUTPUT);
  pinMode(LB, OUTPUT);

  pinMode(RA, OUTPUT);
  pinMode(RB, OUTPUT);

  wifiConnect();

  config.api_key = API_KEY;
  config.database_url = DATABASE_URL;
  auth.user.email = USER_EMAIL;
  auth.user.password = USER_PASSWORD;
  config.token_status_callback = tokenStatusCallback;

  Firebase.begin(&config, &auth);
  Firebase.reconnectWiFi(true);
}
void loop() 
{
  if (Firebase.RTDB.getString(&fbdo, "/control"))
  {
    String controlValue = fbdo.stringData();
    int dataIn = controlValue.toInt();
    Serial.println(dataIn);
    switch(dataIn)
    {
      case 0:stp();
      break;
      case 1:fwd();
      break;
      case 2:bwd();
      break;
      case 3:lft();
      break;
      case 4:ryt();
      break;
    }
  }
}