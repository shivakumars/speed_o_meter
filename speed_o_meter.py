import RPi.GPIO as GPIO
import time
from time import sleep

GPIO.setmode(GPIO.BOARD)
doorState = False
DOOR_SENSOR = 7
doorActive = False
WHEEL_CIRCUMFERENCE = 0.0003

GPIO.setwarnings(True)

GPIO.setup(DOOR_SENSOR, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

currentTime = float(round(time.time()*1000))
prevTime = float(round(time.time()*1000))

while True:
	try:
		doorActive=GPIO.input(DOOR_SENSOR)

		if(doorActive == True):
			currentTime = float(round(time.time()*1000))
			diff = currentTime - prevTime
			diff = ((diff / 1000)/3600)
			prevTime = currentTime
			if(diff!=0):
				speed = WHEEL_CIRCUMFERENCE / diff
				if(speed<120):
					print "running in " + str(speed) +"km/hr"
		sleep(0.01)
	except KeyboardInterrupt:
		GPIO.cleanup()

GPIO.cleanup()