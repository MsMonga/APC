import serial
import time

ser = serial.Serial('/dev/ttyUSB0', 9600, timeout=0.2)   # the same 9600 as the sketch
time.sleep(2)
ser.reset_input_buffer()
print("serial ok")
ser.close()
