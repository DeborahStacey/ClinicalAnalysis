## main.py
# Primary Owner: Clinical Analysis Team

import checkPythonVersion
import processRequest
import parseCLA
import socket
import sys
import os


###
### Check python version running this script
###
checkPythonVersion.ConfirmPythonVersion3()


###
### Get command line args (host and port)
###
host, port = parseCLA.Server_HostPort()


###
### Save this sessions settings to text file
###
f = open("pidport.conf", 'w')
f.write(str(os.getpid()) + "," + str(port))
f.close()


###
### Setup the socket
###
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((host, port))


###
### Main program loop (wait for a request)
###
while True:
    s.listen(1)
    conn, addr = s.accept()
    print('Connected by', addr)

    try:
        rawData = conn.recv(1024)
        if not rawData: continue


        data = rawData.decode('utf-8')

        completedRequest = processRequest.ProcessRequest(data)


        if(completedRequest == None):
            returnMsg = "ERROR: completed request was none"
            conn.sendall(returnMsg.encode('utf-8'))
        else:
            print("Completed request is:\n" + completedRequest)
            conn.sendall(completedRequest.encode('utf-8'))

        conn.close()
    except socket.error:
        print("Error Occured. Did a client connect but not send anything?")
        continue
