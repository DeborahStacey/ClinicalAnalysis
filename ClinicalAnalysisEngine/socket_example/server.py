import socket

host = ''        # Symbolic name meaning all available interfaces
port = 12345     # Arbitrary non-privileged port
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((host, port))

print(host , port)



while True:
    s.listen(1)
    conn, addr = s.accept()
    print('Connected by', addr)

    try:
        data = conn.recv(1024)
        msg = data.decode('utf-8')

        if not data: continue 

        print("Client Says: " + msg)

        msgToSend = "The server says you sent: " + msg 
        conn.sendall(msgToSend.encode('utf-8'))

    except socket.error:
        print("Error Occured.")
        break

conn.close()
