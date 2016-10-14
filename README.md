# ClinicalAnalysis










##### Directory: ClinicalAnalysisEngine/socket_example ---------------------------------------------------------------------------------------------------------------------
Running: client on local machine, and connecting to server in the cloud:
	1. Run client.py ($ python3 client.py)
	2. Type a message into the client.py's prompt, and the message will be sent using sockets to the server.py script,
           the server.py will then send the message back to client.py

Running both client and server on local machine:
	1. Run server.py in one terminal ($ python3 server.py),
	2. Run client.py in a second terminal with localhost as the first argument ($ python3 client.py localhost)
	3. Type a message into the client.py's prompt, and the message will be sent through the socket, to server.py, and server.py
           will send the message back to client.py 


Sockets will be used to connect the front end team, to the analysis team.
The client represents the front end team, and the server represents the clinical analysis team.
The front end team will use json over sockets to make requests for analysis. The clinical team will then send
the results back over the socket.

