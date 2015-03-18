/* Reads the voltage output from an LM35
and converts the voltage to a temperature C.
The analog input: 0 - 1023
Vs: 5V
LM35 output: 10mV/C
*/

int inputPin = A0;     // LM35 output connected to Analog pin0
int inputValue = 0;    // analog sensor value 0 to 1023
float temperature = 0; //initialize temperature variable
char tempValue[]="";

void setup() {
  // inputPin is an INPUT
  pinMode(inputPin, INPUT);  
  Serial.begin(9600);
  
}

void loop() {
  // read the voltage from the LM35
  inputValue = analogRead(inputPin);
  
  //map the analog reading of the LM35 based on a Vs: 5V and Vin: 10mV/C 
  temperature=(float(inputValue)/1023.0)*500.0;
  //print to USB
  Serial.print("Temperature: ");
  Serial.println(temperature,1);
  
}
