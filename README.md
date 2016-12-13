#### December 13th, 2016

## Connecting our client to the cloud / default host
To connect to the default server with our client, run: `adhoctesting.py`, upon running this command, you will be given a list of tests that can be run. Rerun `adhoctesting.py` with the test of your choice, example: `python3 adhoctesting.py simple/1` will run the simple/1 test.

## Setup local server (clinical analysis engine)
To start the server locally, run the file: `python3 startMain.py`
To stop the server locally, run the file: `python3 stopMain.py`

**NOTE:** startMain.py will need permissions to create and modify files, or else it will not be able to save the PID (process id) of the server process. This means that stopMain.py will not be able to kill the server process. 

Without `startMain.py` being able to create and modify files, `stopMain.py` won't have a file to read in order to figure out what PID should be killed. In this case, you will need to run `ps ax` and find the PID from the list of processes, and then `kill <PID>` to manually kill the server process.

**NOTE:** if you are running `python3 startMain.py` and nothing is happening, either check the bottom of the file: `errors.main.py` or run `python3 main.py` directly to see what errors are occurring.

## Specifying a custom host
To connect to a custom ip with our client, run the command `python3 adhoctesting.py -h <host ip>`,

## Connect our client to a server being run locally
To connect to a local server with our client, run the command `python3 adhoctesting.py -h localhost`,

## Specifying a custom port
To connect using a custom port, use the `-p` flag, example: `python3 adhocteting.py -p <port>`
