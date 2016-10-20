import socket
import sys


#default info to connect to our server
host = '104.196.166.63'        # IP of the server
port = 12345                   # The same port as used by the server


#Check python version running this script
version = sys.version.split(".")[0]
if(version == "2"):
    print("\nPlease run this script using python3,\n    quiting...\n")
    quit()


argCount = len(sys.argv) - 1 #Number of CL args not counting program name

if(argCount >= 1): #user has provdied ip address
        host = sys.argv[1]
        print("Setting server ip to: " + host)

if(argCount >= 2): #user has provided port
        port = sys.argv[2]
        print("Setting sever port to: " + port)


#Setup socket, and connect to server
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host, port))


#Send Message
userInput = input("Enter fields, space delimited: ")
fields = userInput.split(" ")

jsonMessage = '{"operation": "lookup", "animals": "all", "field": ['

for field in fields:
    jsonMessage += '"' + field + '", ' 

jsonMessage = jsonMessage[:-2]

jsonMessage += ']}'

print(jsonMessage)
s.sendall(jsonMessage.encode('utf-8'))


#Recieve response from server
data = s.recv(1024)
print('From server (', data.decode('utf-8'), ')')


s.close()


