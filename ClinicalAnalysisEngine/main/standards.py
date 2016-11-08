## standards.py
# Primary Owner: Alex Eckensweiler

import json

def InvalidJSON():
    return Return(INVALID_JSON_CODE, INVALID_JSON_MESSAGE)

def InvalidOperation():
    return Return(INVALID_OPERATION_CODE, INVALID_OPERATION_MESSAGE)

def MissingOperation():
    return Return(MISSING_OPERATION_CODE, MISSING_OPERATION_MESSAGE)

def MissingAnimal():
    return Return(MISSING_ANIMAL_CODE, MISSING_ANIMAL_MESSAGE)

def MissingField():
    return Return(MISSING_FIELD_CODE, MISSING_FIELD_MESSAGE)

def CaughtException():
    return Return(EXCEPTION_CODE, EXCEPTION_MESSAGE)

def SocketError():
    return Return(SOCKET_ERROR_CODE, SOCKET_ERROR_MESSAGE)

def InvalidPort():
    return Return(INVALID_PORT_CODE, INVALID_PORT_MESSAGE)

INVALID_JSON_CODE = 'ERROR_01'
INVALID_JSON_MESSAGE = "Invalid json request, improperly formatted json"

INVALID_OPERATION_CODE = 'ERROR_02'
INVALID_OPERATION_MESSAGE = 'Invalid operation selected'

INVALID_OPERATOR_CODE = 'ERROR_04'
INVALID_OPERATOR_MESSAGE = 'Invalid operator selected'

MISSING_OPERATION_CODE = 'ERROR_10'
MISSING_OPERATION_MESSAGE = "Invalid json request, missing key: operation"

MISSING_ANIMAL_CODE = 'ERROR_11'
MISSING_ANIMAL_MESSAGE = "Invalid json request, missing key: animal"

MISSING_FIELD_CODE = 'ERROR_12'
MISSING_FIELD_MESSAGE = "Invalid json request, missing key: field"

SOCKET_ERROR_CODE = 'ERROR_20'
SOCKET_ERROR_MESSAGE = "There was a socket error"

INVALID_PORT_CODE = 'ERROR_21'
INVALID_PORT_MESSAGE = "User has entered incorrect port"

EXCEPTION_CODE = 'ERROR_99'
EXCEPTION_MESSAGE = "Exception caught"

def Return(code, message):
    jsonMsg = {}
    jsonMsg["result"] = "error"
    jsonMsg["code"] = code
    jsonMsg["message"] = message
    return json.dumps(jsonMsg)
