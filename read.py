#!/usr/bin/env python

import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522

reader = SimpleMFRC522()

try:
        print("Scan RFID chip...")
        id = reader.read()[0]
        print("The ID for this card is:", id)
        
finally:
        GPIO.cleanup()
