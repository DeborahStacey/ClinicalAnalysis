# ClinicalAnalysis

## Usage
### Directory: ClinicalAnalysisEngine/main 
DATE: Oct 21st, 2016

#### Description:
It is now possible to send a json request with three required key parameters: "operation", "animals", and "field". If "weight" and/or "height" is sent as values of "field", then mock data for "weight" and/or "height" data will be sent back. The next step is to replace the mock data, with actual data grabbed from the database.
####Connect to Google cloud instance:
Parameter based input: `$ python3 fieldPoke.py`

Freeform user input: `$ python3 client.py`

####Run entirely locally:
Start the clinical analysis engine locally: `$ ./startServer.sh`

Stop the local clinical analysis engine: `$ ./stopServer.sh`

Run client (freeform user input): `$ python3 client.py localhost`

Run client (parameter based input): `$ python3 fieldPoke.py localhost`



### Directory: ClinicalAnalysisEngine/socket_example 
DATE: Oct 14th, 2016
#####Running: client on local machine, and connecting to server in the cloud:
1. Run client.py 
`$ python3 client.py`
2. Type a message into the client.py's prompt, and the message will be sent using sockets to the server.py script,
   the server.py will then send the message back to client.py

#####Running both client and server on local machine:
1. Run server.py in one terminal: `$ python3 server.py`
2. Run client.py in a second terminal with localhost as the first argument: `$ python3 client.py localhost`
3. Type a message into the client.py's prompt, and the message will be sent through the socket, to server.py, and server.py
   will send the message back to client.py 
