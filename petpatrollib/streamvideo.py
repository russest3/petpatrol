import os
import psutil

PROCNAME = 'motion'

def checkIfProcessRunning(processName):
    '''
    Check if there is any running process that contains the given name processName.
    '''
    #Iterate over the all the running process
    for proc in psutil.process_iter():
        try:
            # Check if process name contains the given name string.
            if processName.lower() in proc.name().lower():
                return True
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass
    return False

def streamvideo():
  if checkIfProcessRunning(PROCNAME):
    print("Streaming service already started.  Do you want to stop it? (y/n)")
    running = True
    answer = str(input("> "))
    if answer == "y" or answer == "Y":
      for proc in psutil.process_iter():
        if proc.name() == PROCNAME:
          os.system("sudo service motion stop")
          running = False
  else:
    running = False

  if running == False or alreadystoppedit != True:
    print("Start video streaming? (y/n)")
    _start = str(input("> "))
    if _start == "y" or _start == "Y":
      os.system("sudo service motion start")
    
    if checkIfProcessRunning('raspivid'):
      print("Video streaming has started")
      return True
    else:
      print("Streaming service failed to start.")
      return False
