#!/usr/bin/env python3

import sys
import serial
import time

port = '/dev/ttyUSB0'
if len(sys.argv) >= 2:
    port = sys.argv[1]

# Connect to serial device at 115200 baud (matches arduino speed)
ser = serial.Serial(port, 115200, timeout=1.0)
ser.read(1000)  # empty read buffer
ser.flush()

print('disable all the actuators')
for i in range(1, 7):
    ser.write('Cs{},24,0\n'.format(i).encode())  # Torque Disable
    time.sleep(0.3)
    ser.flush()

print('set the actuator torque limits')
for i in range(1, 7):
    ser.write('CS{},34,1023\n'.format(i).encode())  # Torque Limit 50%
    time.sleep(0.3)
    ser.flush()

print('enable all the actuators')
for i in range(1, 7):
    ser.write('Cs{},24,1\n'.format(i).encode())  # Torque Enable
    time.sleep(0.3)
    ser.flush()

print('go to resting position')
rest = [2048, 1000, 1100, 1700, 512, 512]
for i, val in enumerate(rest):
    ser.write('CS{},30,{}\n'.format(i+1, val).encode())  # Goal position
    time.sleep(0.3)
    ser.flush()

print('disable all the actuators')
for i in range(1, 7):
    ser.write('Cs{},24,0\n'.format(i).encode())  # Torque Disable
    time.sleep(0.3)
    ser.flush()

ser.read(1000) # empty read buffer
print('read present position')
for i in range(1, 7):
    ser.write('CG{},36\n'.format(i).encode())  # Torque Limit
    print(ser.readline())
    time.sleep(0.3)
