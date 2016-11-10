#!/usr/bin/env python3
## startMain.py
# Primary Owner: Andrew Downie

from cautils import checkPythonVersion
import subprocess 
import sys

from os.path import abspath, dirname, join
import os


PID_EXISTS = 0 #Magic number that makes os.kill check for existance of a process
pidportfile = "pidport.conf"

###
### Start main.py as subprocess
###
def StartMainPy():
    errPath = abspath(join(dirname(__file__), 'errors.main.py'))
    logPath = abspath(join(dirname(__file__), 'log.main.py'))
    mainPath = abspath(join(dirname(__file__), 'main.py'))


    print("\nStarting clinical analysis engine...\n")
    with open(errPath, "a+") as err, open(logPath, "a+") as log:
        commandList = ["python3", "-u", mainPath]
        print(commandList)

        subprocess.Popen(commandList, stderr=err, stdout=log)

###
### Check python version running this script
###
checkPythonVersion.ConfirmPythonVersion3()


###
### Get the pid of the last run 
###                   
pid = 0 
absPathPidPortFile = abspath(join(dirname(__file__), pidportfile))

if os.path.isfile(absPathPidPortFile):
    with open(absPathPidPortFile) as f:
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
