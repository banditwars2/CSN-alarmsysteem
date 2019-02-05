from gpiozero import LED
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(4, GPIO.IN, pull_up_down=GPIO.PUD_UP)

greenLed = LED(6)           # pin number of the green LED
yellowLed = LED(19)         # pin number of the yellow LED
redLed = LED(26)            # pin number of the red LED

# Before running the script, let the PIR adapt to its surrounding (or set it in a cup)
#pir = MotionSensor(27)

def start_up():
    'shows a pattern of blinking LED\'s, to show the client is connected to host'
    redLed.on()
    time.sleep(1)
    yellowLed.on()
    time.sleep(1)
    greenLed.on()
    test(3)


def test(xTimes):
    'turn all the LEDs and turn them off for xTimes'
    count = 0
    while count < xTimes + 1:
        greenLed.on()
        yellowLed.on()
        redLed.on()
        time.sleep(1)

        greenLed.off()
        yellowLed.off()
        redLed.off()
        time.sleep(1)
        count += 1

start_up()
while True:
    input_state = GPIO.input(4)
    if input_state == False:
        print('Button Pressed')
        time.sleep(0.2)
