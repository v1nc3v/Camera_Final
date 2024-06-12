# Vincent Ton
# June 11, 2024
# This script controls the servo motor movement

import sys
import time
import RPi.GPIO as GPIO

def main(argv):
    start = argv[1]
    end = argv[2]
    delay = argv[3]
    loop = argv[4]
    servoMotor = argv[5]
    
    # Horizontal movement
    if (servoMotor == 1)
	# Setup GPIO numbering mode and set pin 11 as output
	GPIO.setmode(GPIO.BOARD)
	GPIO.setwarnings(False)
	GPIO.setup(11, GPIO.OUT)
	
	# Start PWM running but have the pulse off initially
	servo = GPIO.PWM(11, 50)
	servo.start(0)
    # Vertical movement
    else:
	# Setup GPIO numbering mode and set pin 13 as output
	GPIO.setmode(GPIO.BOARD)
	GPIO.setwarnings(False)
	GPIO.setup(13, GPIO.OUT)
	
	# Start PWM running but have the pulse off initially
	servo = GPIO.PWM(13, 50)
	servo.start(0)
	    
    for i in range(0, int(loop)):
	# Pass in a starting and ending degree depending on the button pressed
        for dc in range(int(start), int(end), 1):
            servo.ChangeDutyCycle(2 + (dc / 18))
            time.sleep(float(delay))
            servo.ChangeDutyCycle(0)
            time.sleep(1)
            print("Turning to " + dc + " degrees.")

    servo.stop()
    GPIO.cleanup()
