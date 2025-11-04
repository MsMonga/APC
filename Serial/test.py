import serial
import time

ser= serial.Serial('/dev/ttyUSB0', 9600, timeout=1.0)
time.sleep(3)
ser.reset_input_buffer()
print("serial ok")

ser.close()
