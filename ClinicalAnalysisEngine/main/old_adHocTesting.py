## adHocTesting.py
# Primary Owner: Andrew Downie

import checkPythonVersion
import parseCLA
import socket
import sys


#####
##### Available Tests
#####
jsonFront = '{"operation": "operation-here", "animals": "animal-here", "field": ['
jsonBack = ']}'

availableTests = {
    'simple1': '{"age":{"gt":5}}',
    'layered1':'{ "$and": [{ "age": { "eq": 5 } }, { "weight": { "lt": 20 } }, { "$or": [{ "height": { "eq": 20 } }, { "length": { "eq": 20 } } ] } ] }',
    'broken1': '{ "$and": [{ "age": { "eq": 5 } }, { "weight": { "lt": 20 } }, { "$or": [{ "height": { "eq": 20 } }, { "length": { "eq": 20 } }] }, { "$or": [{ "height": { "eq": 20 } }, { "length": { "eq": 20 } }] }] }'
}




###
### SelectTest
###
def SelectTest(testName):
    try:
        jsonMiddle = availableTests[testName]
    except:
        print("That test was not found")
        quit()
    jsonFull = jsonFront + jsonMiddle + jsonBack
    print("Sending: \n" + jsonFull + "\n")
    return jsonFull

###
### Check python version running this script
###
checkPythonVersion.ConfirmPythonVersion3()

###
### Get CLA args
###
host, port, testName = parseCLA.HostPortData()

###
### Show the settings the user has selected
###
print("Host set to: " + host)
print("Port set to: " + str(port))
print("Test set to: " + str(testName))

###
### Explain how to select which test to run
###
if(testName == ""):
    print("\n\nYou need to choose a test...")
    print("Available precanned json tests are:")
    for key, value in availableTests.items() :
        print ("\t" + key)

    print("\nexiting...")
    quit()

#Setup socket, and connect to server
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host, port))


#Run the selected test
print("\nRunning test: " + testName + "\n")
s.sendall(SelectTest(testName).encode('utf-8'))


#Recieve response from server
data = s.recv(1024)
print('From server (', data.decode('utf-8'), ')')


s.close()
