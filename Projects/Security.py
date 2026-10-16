from gpiozero import LED, Button, MotionSensor
from time import sleep
from adafruit_servokit import ServoKit

# Create an LED object on GPIO 17
led = LED(17)
button = Button(27)
pir = MotionSensor(4)
kit = ServoKit (channels=16)
kit.servo[0].set_pulse_width_range(500, 2400)
kit.servo[0].actuation_range = 180

try:
    while True:
        print(pir.motion_detected)
        if pir.motion_detected:
            print("Motion detected!")
            led.on()

           
            kit.servo[0].angle = 90
    
            sleep(1)
            kit.servo[0].angle = 0

        else:
            print("No motion")
            led.off()
            kit.servo[0].angle = 0
        
       
        
except KeyboardInterrupt:
    print("\nProgram stopped by user")
    led.off()
    
   
