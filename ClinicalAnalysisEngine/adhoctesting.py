## adHocTesting.py
# Primary Owner: Andrew Downie

from cautils import checkPythonVersion
from cautils import socketRequest
from cautils import parseCLA
import json
import sys
import os

testFolder = "Adhoctests"



###
### Check python version running this script
###
checkPythonVersion.ConfirmPythonVersion3()


###
### Get CLA args
###
host, port, testName = parseCLA.HostPortData("Testname")


###
### List test names
###
if(testName == ""):
    print("\nYou must select a test, valid testnames are:")

    for filename in os.listdir(testFolder):
        print("\t" +filename)

    print("\nExiting...\n")
    quit()


###
### Load the selected test from the file with the coresponding name into a string
###
testFilePath = os.path.join(testFolder, testName)
try:
    testFile = open(testFilePath, "r")
    testJson = testFile.read()
except:
    print("Error opening test file: " + testFilePath + ",\n\tquiting...\n")
    quit()


###
### Send the json string, and wait for a response
###
result = socketRequest.JsonRequest(host, port, testJson)
print("\n\nResult from server:\n" + result)
