#!/usr/bin/python

import time
import sys
sys.path.append("sensor")
sys.path.append("motor")
import motor_control as motor
import ultrasonic_distance as sensor


def driver():
	try:
		motor.setup()
	except:
		return
	while True:
		if sensor.distance() > 10:
			motor.forward(0.5)
		else:
			motor.stop()
		time.sleep(0.5)

def main():
	try:
		driver()
	motor.stop()
	motor.cleanup()

if __name__ == "__main__":
	main()
