// Define pin connections & motor's steps per revolution
const int dirPin1 = 2;
const int stepPin1 = 3;
const int dirPin2 = 4;
const int stepPin2 = 5;
const int stepsPerRevolution = 100;
int motion;

void setup()
{
  // Declare pins as Outputs
  pinMode(stepPin1, OUTPUT);
  pinMode(dirPin1, OUTPUT);
  pinMode(stepPin2, OUTPUT);
  pinMode(dirPin2, OUTPUT);
  Serial.begin(115200);
}
void loop()
{
  if (Serial.available() > 0) {
    // read the incoming byte:
    motion = Serial.read();
    if(motion == 'x') spinx();
    if(motion == 'y') spiny();
    if(motion == 'X') spinNx();
    if(motion == 'Y'){
      digitalWrite(dirPin2, LOW);
      for(int y = 0; y < stepsPerRevolution*10; y++)
      {
        digitalWrite(stepPin2, HIGH);
        delayMicroseconds(1000);
        digitalWrite(stepPin2, LOW);
        delayMicroseconds(1000);
      }
    
    }
  }
}

void spinx()
{
  digitalWrite(dirPin1, HIGH);
  for(int x = 0; x < stepsPerRevolution; x++)
  {
    digitalWrite(stepPin1, HIGH);
    delayMicroseconds(1000);
    digitalWrite(stepPin1, LOW);
    delayMicroseconds(1000);
  }
}

void spinNx()
{
  digitalWrite(dirPin1, LOW);
  for(int x = 0; x < stepsPerRevolution; x++)
  {
    digitalWrite(stepPin1, HIGH);
    delayMicroseconds(1000);
    digitalWrite(stepPin1, LOW);
    delayMicroseconds(1000);
  }
}

void spiny()
{
  digitalWrite(dirPin2, HIGH);
  for(int x = 0; x < stepsPerRevolution; x++)
  {
    digitalWrite(stepPin2, HIGH);
    delayMicroseconds(1000);
    digitalWrite(stepPin2, LOW);
    delayMicroseconds(1000);
  }
}
