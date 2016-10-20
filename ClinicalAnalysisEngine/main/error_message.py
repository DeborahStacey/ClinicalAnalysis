import json



def Return(code, message):
    message = {}
    message["code"] = code
    message["message"] = message
    message["result"] = "error"
    return json.dumps(message)
