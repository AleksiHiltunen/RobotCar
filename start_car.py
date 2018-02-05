#!/usr/bin/python3

import time
import os
import sys
import random
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
		while s.distance() > 30:
			m.forward()
			if s.distance() > 3000:
				m.stop()
				m.back(1)
				m.stop()
				break
			time.sleep(0.2)

		m.stop()
		#m.back(1)
		m.stop()
		turn = random.sample(["right", "left"], 1)
		turn = turn[0]
		while s.distance() < 70:
			if turn == "right":
				m.right()
			elif turn == "left":
				m.left()
			time.sleep(0.2)

		m.stop()
		time.sleep(0.1)

def main():
	try:
		driver()
	except:
		sys.exit(1)

if __name__ == "__main__":
	main()
