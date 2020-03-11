import datetime
import os.path
from os import path

def takephoto():
    x = datetime.datetime.now()
    filename = str(x.year) + '-' + str(x.month) + '-' + str(x.day) + '-' + str(x.hour) + '-' + str(x.minute) + '.jpg'
    command = 'raspistill -o photos/' + filename
    os.system(command)

    mypath = 'photos/' + filename
    if path.exists(mypath):
        print("Photo " + filename + " taken")
        return True
    else:
        print("Failed to take photo")
        return False