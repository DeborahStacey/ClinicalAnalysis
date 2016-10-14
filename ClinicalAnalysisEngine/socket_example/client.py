import socket

host = '104.196.166.63'
port = 12345                   # The same port as used by the server
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host, port))

userInput = input("Enter a message to send to the server: ");

s.sendall(userInput.encode('utf-8'))

data = s.recv(1024)
print('From server (', data.decode('utf-8'), ')')


s.close()

