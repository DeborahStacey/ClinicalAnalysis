## error_message.py
# Primary Owner: Andrew Downie

import json

def Return(code, message):
    jsonMsg = {}
    jsonMsg["result"] = "error"
    jsonMsg["code"] = code
    jsonMsg["message"] = message
    return json.dumps(jsonMsg)
