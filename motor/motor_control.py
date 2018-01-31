# Import required libraries
import sys
import time
import RPi.GPIO as GPIO
from multiprocessing import Process

# Use BCM GPIO references
# instead of physical pin numbers
#GPIO.setmode(GPIO.BCM)
mode=GPIO.getmode()
GPIO.cleanup()

# Define GPIO signals to use
# Physical pins 11,15,16,18
# GPIO17,GPIO22,GPIO23,GPIO24

StepLeftPinForward=16
StepLeftPinBackward=18
StepRightPinBackward=13
StepRightPinForward=15

sleeptime=1

GPIO.setmode(GPIO.BOARD)
GPIO.setup(StepLeftPinForward, GPIO.OUT)
GPIO.setup(StepLeftPinBackward, GPIO.OUT)
GPIO.setup(StepRightPinForward, GPIO.OUT)
GPIO.setup(StepRightPinBackward, GPIO.OUT)

def setup():
    StepLeftPinForward=16
    StepLeftPinBackward=18
    StepRightPinBackward=13
    StepRightPinForward=15

    sleeptime=1

    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(StepLeftPinForward, GPIO.OUT)
    GPIO.setup(StepLeftPinBackward, GPIO.OUT)
    GPIO.setup(StepRightPinForward, GPIO.OUT)
    GPIO.setup(StepRightPinBackward, GPIO.OUT)

def _left_forward(x):
    GPIO.output(StepLeftPinForward, GPIO.HIGH)
    time.sleep(x)
    GPIO.output(StepLeftPinForward, GPIO.LOW)

def _left_back(x):
    GPIO.output(StepLeftPinBackward, GPIO.HIGH)
    time.sleep(x)
    GPIO.output(StepLeftPinBackward, GPIO.LOW)


def _right_forward(x):
    GPIO.output(StepRightPinForward, GPIO.HIGH)
    time.sleep(x)
    GPIO.output(StepRightPinForward, GPIO.LOW)

def _right_back(x):
    GPIO.output(StepRightPinBackward, GPIO.HIGH)
    time.sleep(x)
    GPIO.output(StepRightPinBackward, GPIO.LOW)


def forward(x):
    left_f = Process(target = _left_forward(x))
    right_f = Process(target = _right_forward(x))
    left_f.start()
    right_f.start()

def back(x):
    left_b = Process(target = _left_back(x))
    right_b = Process(target = _right_back(x))
    left_b.start()
    right_b.start()

def left(x):
    GPIO.output(StepLeftPinBackward, GPIO.HIGH)
    time.sleep(x)
    GPIO.output(StepLeftPinBackward, GPIO.LOW)

def right(x):
    GPIO.output(StepRightPinBackward, GPIO.HIGH)
    time.sleep(x)
    GPIO.output(StepRightPinBackward, GPIO.LOW)


def cleanup():
    GPIO.cleanup()

GPIO.cleanup()
