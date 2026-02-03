void fwd()
{
  digitalWrite(LA, HIGH);
  digitalWrite(LB, LOW);

  digitalWrite(RA, HIGH);
  digitalWrite(RB, LOW);
  Serial.println("Moving Fwd");
}
void bwd()
{
  digitalWrite(LA, LOW);
  digitalWrite(LB, HIGH);

  digitalWrite(RA,LOW);
  digitalWrite(RB, HIGH);
  Serial.println("Moving Bwd");
}
void lft()
{
  digitalWrite(LA, LOW);
  digitalWrite(LB, HIGH);

  digitalWrite(RA, HIGH);
  digitalWrite(RB, LOW);
  Serial.println("Moving Lft");
}
void ryt()
{
  digitalWrite(LA, HIGH);
  digitalWrite(LB, LOW);

  digitalWrite(RA,LOW);
  digitalWrite(RB, HIGH);
  Serial.println("Moving ryt");
}
void stp()
{
  digitalWrite(LA, LOW);
  digitalWrite(LB, LOW);

  digitalWrite(RA, LOW);
  digitalWrite(RB, LOW);
  Serial.println("Stopped");
}