## main.py
# Primary Owner: Andrew Downie

import checkPythonVersion
import sys
import os


###
### Check python version running this script
###
checkPythonVersion.ConfirmPythonVersion3()

SIGKILL = 9 #Magic number for killing a process

###
### Load this sessions settings from pidport.conf
###                    (that way we can kill the main.py script running local to this folder, but leave the other main.py's running on the same computer but on other ports)
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
            print("\nUnable to kill process, either:\n - it was already stopped,\n - it was never running,\n - pid in pidport.conf file is wrong\n")
