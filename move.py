import RPi.GPIO as GPIO
from time import sleep
import os
import sys

def moveit():
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

  try:
    direction = input("> ")
    if direction != "f" or direction != "f" or direction != "b" or direction != "B" or direction != "l" or direction != "L" or direction != "r" or direction != "R":
      raise Exception()
  except Exception:
    print("Please enter one of the options listed")

  print("\nOK!  How far? (1 - 10)")

  try:
    distance = int(input("> "))
    if distance > 10:
      raise Exception()
  except:
    print("Please enter a number between 1-10")

  if direction == "f" or direction == "F":
    l = GPIO.PWM(left, 50)
    l.start(0)
    r = GPIO.PWM(right, 50)
    r.start(0)
    l.start(12)
    r.start(2)
    sleep(distance)
    l.stop()
    r.stop()
    GPIO.cleanup()

  if direction == "b" or direction == "B":
    l = GPIO.PWM(left, 50)
    r = GPIO.PWM(right, 50)
    l.start(2)
    r.start(12)
    sleep(distance)
    l.stop()
    r.stop()
    GPIO.cleanup()
