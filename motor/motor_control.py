#!/usr/bin/python3

# Import required libraries
import sys
import time
import RPi.GPIO as GPIO
import threading

class Motor():
	def __init__(self):
		self.StepLeftPinForward=23
		self.StepLeftPinBackward=24
		self.StepRightPinBackward=27
		self.StepRightPinForward=22
		mode=GPIO.getmode()
		GPIO.setmode(GPIO.BCM)
		GPIO.setup(self.StepLeftPinForward, GPIO.OUT)
		GPIO.setup(self.StepLeftPinBackward, GPIO.OUT)
		GPIO.setup(self.StepRightPinForward, GPIO.OUT)
		GPIO.setup(self.StepRightPinBackward, GPIO.OUT)


	def left_forward(self):
		GPIO.output(self.StepLeftPinForward, GPIO.HIGH)
		time.sleep(x)

	def left_back(self):
		GPIO.output(self.StepLeftPinBackward, GPIO.HIGH)

	def right_forward(self):
		GPIO.output(self.StepRightPinForward, GPIO.HIGH)
		time.sleep(x)

	def right_back(self):
		GPIO.output(self.StepRightPinBackward, GPIO.HIGH)

	def right_stop(self):
		GPIO.output(self.StepRightPinBackward, GPIO.LOW)
		GPIO.output(self.StepRightPinForward, GPIO.LOW)

	def left_stop(self):
		GPIO.output(self.StepLeftPinBackward, GPIO.LOW)
		GPIO.output(self.StepLeftPinForward, GPIO.LOW)

	def back(self, x):
		print("Back")
		GPIO.output(self.StepRightPinForward, GPIO.HIGH)
		GPIO.output(self.StepLeftPinForward, GPIO.HIGH)
		time.sleep(x)
		self.stop()

	def forward(self):
		print("Forward")
		left = threading.Thread(name="left_back", target=self.left_back)
		right = threading.Thread(name="right_back", target=self.right_back)
		left.start()
		right.start()

	def stop(self):
		print("Stop")
		self.right_stop()
		self.left_stop()

	def left(self):
		GPIO.output(self.StepLeftPinForward, GPIO.HIGH)

	def right(self):
		GPIO.output(self.StepRightPinForward, GPIO.HIGH)

	def cleanup():
		GPIO.cleanup()
