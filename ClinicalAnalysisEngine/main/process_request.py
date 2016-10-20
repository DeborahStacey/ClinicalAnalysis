## process_request.py
# Primary Owner: Andrew Downie

import json

#####
##### Process Request
#####
def ProcessRequest(jsonRequest):
    loadedJson = ""


    ###
    ### Load the Json request
    ###
    try:
        loadedJson = json.loads(jsonRequest)
    except:
        return("Not valid json request, please check formatting")


    ###
    ### Check that required keys are present
    ###
    if 'operation' not in loadedJson:
        return "Not valid json request, missing key: operation"
    elif 'animals' not in loadedJson:
        return "Not valid json request, missing key: animals"
    elif 'field' not in loadedJson:
        return "Not valid json request, missing key: fields"


    ###
    ### Collect values of required keys 
    ###
    operation = loadedJson['operation']
    animals = loadedJson['animals']
    fields = loadedJson['field']  


    ###
    ### Return mock data related to request fields
    ###
    jsonOutput = {}
    
    if 'weight' in fields:
        jsonOutput['weight'] = [10, 17, 22]

    if 'height' in fields:
        jsonOutput['height'] = [12, 20, 4]


    #return str(fields)
    return json.dumps(jsonOutput)

    
