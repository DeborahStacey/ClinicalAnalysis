## main.py
# Primary Owner: Andrew Downie

import socket
import process_request
import sys


host = ''        # Symbolic name meaning all available interfaces
port = 12345     # Arbitrary non-privileged port



#Check python version running this script
version = sys.version.split(".")[0]
if(version == "2"):
    print("\nPlease run this script using python3,\n    quiting...\n")
    quit() 

#Setup the socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((host, port))

print("Starting server at: " + host + ":" + str(port))


#Main program loop (wait for a request)
while True:
    s.listen(1)
    conn, addr = s.accept()
    print('Connected by', addr)

    try:
        rawData = conn.recv(1024)
        if not rawData: continue 

	


        data = rawData.decode('utf-8')
        #requestResult = process_request.ProcessRequest('{"request": "fart"}') 
        requestResult = process_request.ProcessRequest(data) 
        conn.sendall(requestResult.encode('utf-8'))


    except socket.error:
        print("Error Occured.")
        break

conn.close()




