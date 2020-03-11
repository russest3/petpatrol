#!/usr/bin/env python3
# Requires:
# - sudo apt-get install vlc python3-rpi.gpio python3-pip
# - sudo pip3 install psutil

import os
import sys
import petpatrollib.move
import petpatrollib.streamvideo
import petpatrollib.takephoto
import petpatrollib.takevideo

def main():
  loop = True
  while loop:
    print("\n****************************************************")
    print("This is Pet Patrol.  How would you like to patrol?")
    print("****************************************************\n")

    print("m,M.    MOVE!")
    print("p,P.    TAKE PHOTO!")
    print("v,V.    RECORD VIDEO!")
    print("s,S.    STREAM VIDEO!")
    print("e,E     I\'m done, exit.")
    choice = str(input("> "))

    if choice == "e" or choice == "E":
      loop = False
      sys.exit(0)

    if choice == "m" or choice == "M":
      petpatrollib.move.move()

    if choice == "p" or choice == "P":
      petpatrollib.takephoto.takephoto()

    if choice == "v" or choice == "V":
      petpatrollib.takevideo.takevideo()
    
    if choice == "s" or choice == "S":
      petpatrollib.streamvideo.streamvideo()
    
    continue
