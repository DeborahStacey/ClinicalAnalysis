## startMain.py
# Primary Owner: Andrew Downie

import checkPythonVersion
import subprocess 
import sys
import os


PID_EXISTS = 0 #Magic number that makes os.kill check for existance of a process
pidportfile = "pidport.conf"

###
### Start main.py as subprocess
###
def StartMainPy():
    print("\nStarting clinical analysis engine...\n")
    with open("errors.main.py", "a+") as err, open("log.main.py", "a+") as log:
        subprocess.Popen(["python3", "-u", "main.py"], stderr=err, stdout=log)

###
### Check python version running this script
###
checkPythonVersion.ConfirmPythonVersion3()


###
### Get the pid of the last run 
###                   
pid = 0 

if os.path.isfile(pidportfile):
    with open(pidportfile) as f:
        for line in f:
            processPID = line.split(",")[0]
            try:
                pid = int(processPID)
            except:
                print("\nUnable to parse pid into int, exiting...\n")
                exit()


###
### Check if last runs pid is still running, if its not start main.py in the background (main.py will save its own pid to pidportfile)
###
try:
    os.kill(pid, PID_EXISTS)
except:
    StartMainPy()
else:
    if pid == 0:
        StartMainPy()
    else:
        print("\nmain.py is already running, please run: $ python3 stopMain.py, first if you wish to restart the server\n")
