import RPi.GPIO as GPIO
from time import sleep
import os
import sys

left = 17
right = 22

def _right():
  l = GPIO.PWM(left, 50)
  r = GPIO.PWM(right, 50)
  l.start(0)
  r.start(12)
  sleep(1.2)
  l.stop()
  r.stop()
  GPIO.cleanup()

def _left():
  l = GPIO.PWM(left, 50)
  r = GPIO.PWM(right, 50)
  l.start(4)
  r.start(0)
  sleep(2)
  l.stop()
  r.stop()
  GPIO.cleanup()

def _forward(distance):
  l = GPIO.PWM(left, 50)
  l.start(0)
  r = GPIO.PWM(right, 50)
  l.start(10.7)
  r.start(6.3)
  sleep(distance)
  l.stop()
  r.stop()
  GPIO.cleanup()

def _back(distance):
  l = GPIO.PWM(left, 50)
  r = GPIO.PWM(right, 50)
  l.start(4.2)
  r.start(7.9)
  sleep(distance)
  l.stop()
  r.stop()
  GPIO.cleanup()

def move():
  left = 17
  right = 22

  GPIO.setwarnings(False)
  GPIO.cleanup()
  GPIO.setmode(GPIO.BCM)
  GPIO.setup(left, GPIO.OUT)
  GPIO.setup(right, GPIO.OUT)

  print("\nOK!  Which direction?")
  print("f,F.  FORWARD!")
  print("b,B.  BACK!")
  print("l,L.  LEFT!")
  print("r,R.  RIGHT!")
  
  distance = 100
  direction = input("> ")

  if direction == "f" or direction == "F" or direction == "b" or direction == "B":
    print("\nOK!  How far? (1 - 10)")
    while distance > 10:
      distance = int(input("> "))
      if distance > 10:
        print("Please enter a number between 1-10")

  if direction == "r" or direction == "R":
    _right()

  if direction == "l" or direction == "L":
    _left()

  if direction == "f" or direction == "F":
    _forward(distance)

  if direction == "b" or direction == "B":
    _back(distance)
  
  return True
