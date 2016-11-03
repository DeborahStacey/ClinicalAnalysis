import socket
import sys

BUFFER_SIZE = 1024

def JsonRequest(host, port, jsonData):
    ###
    ### Check jsonData is not empty string
    ###
    if(jsonData == ''):
        print("\nsocketRequest.JsonRequest: jsonData arg was empty string, nothing to send, exiting...")
        quit()

    ###
    ### Setup socket, and connect to server
    ###
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host, port))

    ###
    ### Send data to server
    ###
    s.sendall(jsonData.encode('utf-8'))

    ###
    ### Recieve and return response from server
    ###
    resultData = s.recv(BUFFER_SIZE).decode('utf-8')

    s.close()
    return resultData
