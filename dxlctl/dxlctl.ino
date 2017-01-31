// dxlctl - simple dynamixel control: AX12-A, MX-28, MX-64

// From arbotix library: https://github.com/machinaut/arbotix
#include <ax12.h>

void setup() {
  Serial.begin(115200 /* baud */);  // USB Serial to computer
  Serial.setTimeout(10 /* milliseconds */);  // Timeout waiting for input

  dxlInit(1000000 /* baud */);  // Dynamixel chain serial

  while (!Serial);  // Wait for serial port to connect
}

void loop() {
  if (Serial.find('C')) {
    int cmd;
    while ((cmd = Serial.read()) < 0);  // Wait until command character
    int id = Serial.parseInt();
    while(Serial.read() < 0);  // Skip comma
    int reg = Serial.parseInt();
    while(Serial.read() < 0);  // Skip next character

    int val = -12345;
    switch (cmd) {
      case 's':  // single-byte register write
        val = Serial.parseInt();
        dxlSetRegister(id, reg, val);
      case 'g':  // single-byte register read
        val = dxlGetRegister(id, reg, 1);
        break;
      case 'S':  // double-byte register write
        val = Serial.parseInt();
        dxlSetRegister2(id, reg, val);
      case 'G':  // double-byte register read
        val = dxlGetRegister(id, reg, 2);
        break;
    }

    Serial.print('R');
    Serial.print(id); Serial.print(',');
    Serial.print(reg); Serial.print(',');
    Serial.print(val); Serial.print('\n');
    Serial.flush();
  }
}
