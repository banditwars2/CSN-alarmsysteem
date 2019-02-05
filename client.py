#!/usr/bin/python3
from gpiozero import LED
import RPi.GPIO as GPIO
import requests
import time
import pygame

# setting up the button
GPIO.setmode(GPIO.BCM)
GPIO.setup(4, GPIO.IN, pull_up_down=GPIO.PUD_UP)

# setting up the LED's
greenLed = LED(6)           # pin number of the green LED
yellowLed = LED(19)         # pin number of the yellow LED
redLed = LED(26)            # pin number of the red LED

# setting up the mixer
pygame.mixer.init()
pygame.mixer.music.load('beep-sound.mp3')


# functies voor LED's
def startup():
    ''
    redLed.on()
    time.sleep(1)
    yellowLed.on()
    time.sleep(1)
    greenLed.on()
    blink_all(3)


def blink_all(xTimes):
    ''
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


#
def alarm_on():
    'Alarm is aangezet'

    redLed.off()
    while True:
        greenLed.on()
        input_state = GPIO.input(4)
        if input_state == False:
            greenLed.off()
            print("Alarm has been triggered!")
            count = 0
            while count < 10:
                yellowLed.off()
                time.sleep(1)
                yellowLed.on()
                count += 1
            yellowLed.on()
            while True:
                r = requests.get('{0}/alarmstatus'.format(hostname))
                response = r.text

                # check whether alarm is on or off and respond accordingly
                if response == 'aan':
                    pygame.mixer.music.play()
                    print("woei")
                    time.sleep(1)
                else:
                    print("Het alarm is uitgezet")
                    yellowLed.off()
                    time.sleep(3)
                    break
            break


# Main flow
while True:
    hostIP = input("Wat is het ip-address van de host: ")       # Het ip-address van de host
    hostPort = int(input("Wat is de poort van de host: "))      # De poort van de host
    hostname = 'http://{0}:{1}'.format(hostIP, hostPort)        # De hostname wordt aangemaakt

    try:
        # try to get a connection to the server
        r = requests.get("{0}/isalive".format(hostname))
        if r.text == "alive":
            print("Connected to the server")
            startup()
            break
    except:
        # when a connection can't be acquired
        print("Couldn't connect to server\n")


# Ask the server for the status of the alarm
while True:
    r = requests.get('{0}/alarmstatus'.format(hostname))
    response = r.text

    # check whether alarm is on or off and respond accordingly
    if response == 'aan':
        print("Alarm is aangezet")
        alarm_on()
    else:
        redLed.on()
        time.sleep(1)
