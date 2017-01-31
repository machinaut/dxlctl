#!/usr/bin/env python

import sys
import serial
import time

if len(sys.argv) < 2:
    print('USAGE: {} <serial_port>'.format(sys.argv[0]))
    exit(1)

# Connect to serial device at 115200 baud (matches arduino speed)
ser = serial.Serial(sys.argv[1], 115200)

# Blink all the LEDs a bunch of times
for led in range(100):
    bit = led & 1
    for i in range(1, 7):
        ser.write('Cs{},25,{}\n'.format(i, bit).encode())
        time.sleep(0.1)
