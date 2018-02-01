#!/usr/bin/python3

import time
import os
import sys
my_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.join(my_dir, "sensor"))
sys.path.append("motor")
import motor_control as motor
import ultrasonic_distance as sensor

def driver():
	print("Initializing Motor")
	m = motor.Motor()
	print("Initializing Sensor")
	s = sensor.Sensor()

	while True:
		dist = s.distance()
		print("Distance is", dist)
		if dist > 50:
			m.forward()
		else:
			m.stop()
			m.back(1)
			m.left(1)
		time.sleep(0.1)

def main():
	try:
		driver()
	except:
		sys.exit(1)

if __name__ == "__main__":
	main()
