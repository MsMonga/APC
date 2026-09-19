import serial
import time

ser= serial.Serial('/dev/ttyUSB0', 9600, timeout=1.0)
time.sleep(3)
ser.reset_input_buffer()
print("serial ok, Press ctrl+C in the shell to stop the serial communication")
try:
    while True:
        time.sleep(0.01)
        if ser.in_waiting>0:
            line= ser.readline().decode('utf-8').rstrip()
            print(line)
except KeyboardInterrupt:
    print("Close Serial Communication")
    ser.close()
