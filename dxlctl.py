#!/usr/bin/env python3

import sys
import serial
import time

port = '/dev/ttyUSB0'
if len(sys.argv) >= 2:
    port = sys.argv[1]

# Connect to serial device at 115200 baud (matches arduino speed)
ser = serial.Serial(port, 115200, timeout=0.2)
ser.read(1000)  # empty read buffer
ser.flush()

print('disable all the actuators')
for i in range(1, 7):
    ser.write('Cs{},24,0\n'.format(i).encode())  # Torque Disable
    ser.write('Cg{},24\n'.format(i).encode())  # Torque Disable
    print(ser.read(1000))
    time.sleep(0.3)
print('set the actuator torque limits')
for i in range(1, 7):
    ser.write('CS{},34,1023\n'.format(i).encode())  # Torque Limit 50%
    ser.write('CG{},34\n'.format(i).encode())  # Torque Limit 50%
    print(ser.read(1000))
    time.sleep(0.3)
print('enable all the actuators')
for i in range(1, 7):
    ser.write('Cs{},24,1\n'.format(i).encode())  # Torque Enable
    ser.write('Cg{},24\n'.format(i).encode())  # Torque Enable
    print(ser.read(1000))
    time.sleep(0.3)
print('go to resting position')
rest = [2048, 1000, 1100, 1700, 512, 512]
for i, val in enumerate(rest):
    ser.write('CS{},30,{}\n'.format(i+1, val).encode())  # Goal position
    ser.write('CG{},30\n'.format(i+1).encode())  # Goal position
    print(ser.read(1000))
    time.sleep(0.3)
print('disable all the actuators')
for i in range(1, 7):
    ser.write('Cs{},24,0\n'.format(i).encode())  # Torque Disable
    ser.write('Cg{},24\n'.format(i).encode())
    print(ser.read(1000))
    time.sleep(0.3)
print('read alarm status')
for i in range(1, 7):
    ser.write('Cg{},18\n'.format(i).encode())  # Torque Enable
    print(ser.readline())
    time.sleep(0.3)
print('read torque limit')
for i in range(1, 7):
    ser.write('CG{},34\n'.format(i).encode())  # Torque Limit
    print(ser.readline())
    time.sleep(0.3)
