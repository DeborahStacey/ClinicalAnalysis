#!/usr/bin/env python3
## stopMain.py
# Primary Owner: Andrew Downie

from cautils import checkPythonVersion
import sys


from os.path import abspath, dirname, join
import os

KILL_PROCESS = 9 #Magic number for killing a process
pidportfile = "pidport.conf"

###
### Check python version running this script
###
checkPythonVersion.ConfirmPythonVersion3()


###
### Load this sessions settings from pidport.conf
###                    (that way we can kill the main.py script running local to this folder, but leave the other main.py's running on the same computer but on other ports)
pid = -1

absPathPidPortFile = abspath(join(dirname(__file__), pidportfile))

if os.path.isfile(absPathPidPortFile):
    with open(pidportfile) as f:
        for line in f:
            processPID = line.split(",")[0]
            try:
                pid = int(processPID)
            except:
                print("unable to parse pid into int, exiting...")
                exit()

            try:
                os.kill(pid, KILL_PROCESS)
            except:
                print("\nUnable to kill main.py, either:\n - it was already stopped / it has yet to be run,\n - pid in " + pidportfile + " file is wrong\n")
            else:
                print("\nStopped main.py with pid matching " + pidportfile + " file\n")
                os.remove(pidportfile)
