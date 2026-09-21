# ramp.py — the Pi decides the speed, the Arduino drives the motor.
# Up to full forward, down through stop to full reverse, back to stop.

import serial
import time

ser = serial.Serial('/dev/ttyUSB0', 9600, timeout=0.2)
time.sleep(2)                        # the Uno resets when the port opens

def send(speed):
    ser.write(f'M,{speed}\n'.encode())
    print(f'M,{speed}')

try:
    for speed in range(0, 256, 15):        # 0 -> 255
        send(speed)
        time.sleep(0.1)
    for speed in range(255, -256, -15):    # 255 -> -255
        send(speed)
        time.sleep(0.1)
    for speed in range(-255, 1, 15):       # -255 -> 0
        send(speed)
        time.sleep(0.1)
finally:
    send(0)                              # never leave the motor running
    ser.close()
