## process_request.py
# Primary Owner: Andrew Downie

import json

def ProcessRequest(jsonRequest):
    loadedJson = ""

    #Load the Json request
    try:
        loadedJson = json.loads(jsonRequest)
    except:
        return("Not valid json request, please check formatting")

    #Check that required keys are present
    if 'operation' not in loadedJson:
        return "Not valid json request, missing key: operation"
    elif 'animals' not in loadedJson:
        return "Not valid json request, missing key: animals"
    elif 'fields' not in loadedJson:
        return "Not valid json request, missing key: fields"


    operation = loadedJson['operation']
    animals = loadedJson['animals']
    fields = loadedJson['fields']  

    return str(fields)

    
