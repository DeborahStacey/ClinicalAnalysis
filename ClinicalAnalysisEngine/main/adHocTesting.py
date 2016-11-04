## adHocTesting.py
# Primary Owner: Andrew Downie

import checkPythonVersion
import socketRequest
import parseCLA
import json
import sys
import os

testFolder = "adhocTests"



###
### Check python version running this script
###
checkPythonVersion.ConfirmPythonVersion3()


###
### Get CLA args
###
host, port, testName = parseCLA.HostPortData()


###
### List test names
###
if(testName == ""):
    print("\nYou must select a test, valid testnames are:")

    for filename in os.listdir(testFolder):
        print("\t" +filename)

    print("\nExiting...\n")
    quit()
else:
    print("Selected test is: " + testName + "\n")


###
### Load the selected test from the file with the coresponding name into a string
###
testFile = open(os.path.join(testFolder, testName), "r")
testJson = testFile.read()
print(testJson)


###
### Send the json string, and wait for a response
###
result = socketRequest.JsonRequest(host, port, testJson)
print("\n\n Result from server:\n" + result)
