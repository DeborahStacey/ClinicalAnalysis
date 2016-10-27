## main.py
# Primary Owner: Andrew Downie

import sys
import os


###
### Check python version running this script
###
version = sys.version.split(".")[0]
if(version == "2"):
    print("\nPlease run this script using python3,\n    quiting...\n")
    quit() 


SIGKILL = 9 

###
### Load this sessions settings from pidport.conf 
###                    (that way we can kill the main.py script running local to this folder, but leave the other main.py's running on the same computer on other ports)
with open("pidport.conf") as f:
    for line in f:
        processPID = line.split(",")[0]
        try:
            pid = int(processPID)
        except:
            print("unable to parse pid into int, exiting...")
            exit()
        try:
            os.kill(pid, SIGKILL)
        except:
            print("unable to kill process, either it was already stopped, or pid in config file is wrong")
        

