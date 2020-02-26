from move import moveit
import os
import sys

def main():
  loop = True
  while loop:
    print("\n****************************************************")
    print("This is Pet Patrol.  How would you like to patrol?")
    print("****************************************************\n")

    print("m,M.    MOVE!")
    print("p,P.    TAKE PHOTO!")
    print("v,V.    TAKE VIDEO!")
    print("e,E     I\'m done, exit.")
    choice = str(input("> "))

    if choice == "e" or choice == "E":
      loop = False
      sys.exit(0)

    if choice == "m" or choice == "M":
      moveit()

    if choice == "p" or choice == "P":
      takephoto.takephoto()

    if choice == "v" or choice == "V":
      takevid.takevid()
    
    continue

if __name__ == "__main__":
    main()
