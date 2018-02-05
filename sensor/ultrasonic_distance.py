#!/bin/usr/python3

#Libraries
import RPi.GPIO as GPIO
import time
import math

class Sensor():
	def __init__(self):
		#set GPIO Pins
		self.GPIO_TRIGGER = 18
		self.GPIO_ECHO = 25
		self.GPIO_FAR = 17

		GPIO.setmode(GPIO.BCM)

		#set GPIO direction (IN / OUT)
		GPIO.setup(self.GPIO_TRIGGER, GPIO.OUT)
		GPIO.setup(self.GPIO_ECHO, GPIO.IN)
		GPIO.setup(self.GPIO_FAR, GPIO.OUT)


	def distance(self):
		print("Getting distance")
		try:
			# set Trigger to HIGH
			GPIO.output(self.GPIO_TRIGGER, True)

			# set Trigger after 0.01ms to LOW
			time.sleep(0.00001)
			GPIO.output(self.GPIO_TRIGGER, False)

			StartTime = time.time()
			StopTime = time.time()

			# save StartTime
			while GPIO.input(self.GPIO_ECHO) == 0:
				StartTime = time.time()

			# save time of arrival
			while GPIO.input(self.GPIO_ECHO) == 1:
				StopTime = time.time()

			# time difference between start and arrival
			TimeElapsed = StopTime - StartTime
			# multiply with the sonic speed (34300 cm/s)
			# and divide by 2, because there and back
			distance = (TimeElapsed * 34300) / 2

		except:
			print("Something went wrong..")
			return -1

		distance = math.floor(distance)
		print(distance)
		return distance

if __name__ == '__main__':
	try:
		sensor = Sensor()
		while True:
			dist = sensor.distance()
			print (dist)

			time.sleep(0.5)

		# Reset by pressing CTRL + C
	except KeyboardInterrupt:
		print("Measurement stopped by User")
		GPIO.cleanup()
