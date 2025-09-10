from gpiozero import PWMLED
#from time import sleep
from signal import pause

led=PWMLED(17)
# version 1
'''while True:
    led.value=0
    sleep(1)
    led.value=0.5
    sleep(1)
    led.value=1
    sleep(1) '''

# Version 2 with inbuilt functions
led.pulse()
pause()