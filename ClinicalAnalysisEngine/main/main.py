## main.py
# Primary Owner: Andrew Downie

import socket
import jsonToSqlParms
import sys
import os


host = ''        # Symbolic name meaning all available interfaces
port = 12345     # Arbitrary non-privileged port


###
### Check python version running this script
###
version = sys.version.split(".")[0]
if(version == "2"):
    print("\nPlease run this script using python3,\n    quiting...\n")
    quit()


###
### Check command lines args
###
if(len(sys.argv) >= 2): #A port has been provided
    try:
        port = int(sys.argv[1])
    except:
        print("Given port (arg 1), was not a proper port/integer")



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

print("Starting server at: " + host + ":" + str(port))

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
        sqlParms = jsonToSqlParms.JsonToSqlParms(data)
        conn.sendall(sqlParms.encode('utf-8'))


    except socket.error:
        print("Error Occured. Did a client connect but not send anything?")
        continue

conn.close()
