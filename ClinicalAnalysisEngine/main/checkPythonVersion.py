## checkPythonVersion.py
# Primary Owner: Andrew Downie

import sys

# Makes sure this script is being run by python 3
def ConfirmPythonVersion3():
    version = sys.version.split(".")[0]
    if(version != "3"):
        print("\nPlease run this script using python3,\n    quiting...\n")
        quit()
