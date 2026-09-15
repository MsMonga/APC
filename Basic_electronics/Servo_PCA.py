import time
from adafruit_servokit import ServoKit

kit = ServoKit(channels=16)

# The default range is 750–2250 µs, which only gives an SG90
# about two thirds of its travel. Tell it the truth:
kit.servo[0].set_pulse_width_range(500, 2400)
kit.servo[0].actuation_range = 180

try:
    for angle in range(0, 181, 5):
        kit.servo[0].angle = angle
        time.sleep(0.02)

    for angle in range(180, -1, -5):
        kit.servo[0].angle = angle
        time.sleep(0.02)

finally:
    kit.servo[0].angle = None 