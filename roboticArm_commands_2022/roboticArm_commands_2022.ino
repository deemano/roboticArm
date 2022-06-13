#include <DynamixelShield.h>

#if defined(ARDUINO_AVR_UNO) || defined(ARDUINO_AVR_MEGA2560)
  #include <SoftwareSerial.h>
  SoftwareSerial soft_serial(7, 8); // DYNAMIXELShield UART RX/TX
  #define DEBUG_SERIAL soft_serial
#elif defined(ARDUINO_SAM_DUE) || defined(ARDUINO_SAM_ZERO)
  #define DEBUG_SERIAL SerialUSB 
#else
  #define DEBUG_SERIAL Serial
#endif

// robotic arm servo IDs
const uint8_t DXL_ID_1 = 1;
const uint8_t DXL_ID_2 = 2;
const uint8_t DXL_ID_3 = 3;

const float DXL_PROTOCOL_VERSION = 1.0; // declare servo firmware

DynamixelShield dxl;  // instance of the main library class

// This namespace is required to use Control table variables
using namespace ControlTableItem;

void setup() {
  // set servos communication baud rate & debug baud rate
  DEBUG_SERIAL.begin(115200);
  dxl.begin(1000000);
  
  // Set Port Protocol Version. 
  // This has to match with DYNAMIXEL protocol version.
  dxl.setPortProtocolVersion(DXL_PROTOCOL_VERSION);
  // Get DYNAMIXEL information
//  dxl.ping(DXL_ID_1);
//  dxl.scan();
}

void loop() {
  // set speed:
  dxl.setGoalVelocity(1, 70);
  dxl.setGoalVelocity(2, 70);
  dxl.setGoalVelocity(3, 70);
  
  // check positions:
  int check1 = dxl.getPresentPosition(DXL_ID_1);
  int check2 = dxl.getPresentPosition(DXL_ID_2);
  int check3 = dxl.getPresentPosition(DXL_ID_3);
  int step = 0; // may use this later for precision motion check
  
    // XYZ middle
  dxl.setGoalPosition(DXL_ID_1, 147, UNIT_DEGREE);
  dxl.setGoalPosition(DXL_ID_2, 147, UNIT_DEGREE);
  dxl.setGoalPosition(DXL_ID_3, 147, UNIT_DEGREE);
  delay(5000);
  
  // random position
  dxl.setGoalPosition(DXL_ID_1, 130, UNIT_DEGREE);
  dxl.setGoalPosition(DXL_ID_2, 70, UNIT_DEGREE);
  dxl.setGoalPosition(DXL_ID_3, 150, UNIT_DEGREE); 
  delay(5000);

  // middle again
  dxl.setGoalPosition(DXL_ID_1, 147, UNIT_DEGREE);
  dxl.setGoalPosition(DXL_ID_2, 147, UNIT_DEGREE);
  dxl.setGoalPosition(DXL_ID_3, 147, UNIT_DEGREE);
  delay(5000);

  // showing the working envelope area of the arm:
  dxl.setGoalPosition(DXL_ID_1, 1, UNIT_DEGREE);
  dxl.setGoalPosition(DXL_ID_2, 50, UNIT_DEGREE);
  dxl.setGoalPosition(DXL_ID_3, 50, UNIT_DEGREE);
  delay(7000);
  dxl.setGoalPosition(DXL_ID_2, 147, UNIT_DEGREE);
  dxl.setGoalPosition(DXL_ID_3, 147, UNIT_DEGREE);
  delay(7000);
  dxl.setGoalPosition(DXL_ID_1, 295, UNIT_DEGREE);
  delay(8000);
  

  int home[3] = {240, 200, 120}; // 220
  dxl.setGoalPosition(DXL_ID_1, home[0], UNIT_DEGREE);
  dxl.setGoalPosition(DXL_ID_2, home[1], UNIT_DEGREE);
  dxl.setGoalPosition(DXL_ID_3, home[2], UNIT_DEGREE);
  delay(50000);
  dxl.setGoalPosition(DXL_ID_1, 1, UNIT_DEGREE);
  delay(5000);
    
}
