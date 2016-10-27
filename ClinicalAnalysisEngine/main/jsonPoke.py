import socket
import sys

#####
##### Available Tests
#####
jsonFront = '{"operation": "operation-here", "animals": "animal-here", "field": ['
jsonBack = ']}'
availableTests = {
    'simple1': '{"age":{"gt":5}}',

    'layered1':'{ "$and": [{ "age": { "eq": 5 } }, { "weight": { "lt": 20 } }, { "$or": [{ "height": { "eq": 20 } }, { "length": { "eq": 20 } } ] } ] }'

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
### ParsePort
###
def ParsePort(port):
    try:
        return int(port)
    except Exception as e:
        print("Invalid -p parameter: " + str(e))
        quit()


###
### Default info to connect to our server
###
hostDefault = '104.196.166.63'        # IP of the server
portDefault = 12345                   # The same port as used by the server
host = hostDefault
port = portDefault
testName = ''

###
### Check python version running this script
###
version = sys.version.split(".")[0]
if(version == "2"):
    print("\nPlease run this script using python3,\n    quiting...\n")
    quit()

###
### Get overridable parameters from command line
###
for arg in sys.argv[1:]:
    if(arg[0] == '-'):
        if(arg[1] == 'p'):
            port = ParsePort(arg[2:])
        elif(arg[1] == 'h'):
            host = arg[2:]
    else:
        testName = arg


###
### Show the settings the user has selected
###
if(host == hostDefault):
    print("Host set to: (default host)")
else:
    print("Host set to: " + host)

if(port == portDefault):
    print("Port set to: (default port)")
else:
    print("Port set to: " + str(port))

print("Test set to: " + testName)

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
