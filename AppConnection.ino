void flash()
{
  digitalWrite(LED_BUILTIN, HIGH); 
  delay(100);
  digitalWrite(LED_BUILTIN, LOW);
  delay(100);    
}
void wifiConnect()
{
  WiFi.begin(WIFI_SSID, WIFI_PASSWORD);
  while ((!(WiFi.status() == WL_CONNECTED)))
  {
    flash();
    Serial.print(".");
  }
  Serial.println("WiFi Connected !");
  digitalWrite(LED_BUILTIN, HIGH);
}