## process_request.py
# Primary Owner: Andrew Downie

import error_message
import json
import DeconstructJson

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
    	return error_message.Return(1, "Invalid json request, improperly formatted json")


    ###
    ### Check that required keys are present
    ###
    if 'operation' not in loadedJson:
    	return error_message.Return(10, "Invalid json request, missing key: operation")
    elif 'animals' not in loadedJson:
    	return error_message.Return(11, "Invalid json request, missing key: animals")
    elif 'field' not in loadedJson:
    	return error_message.Return(12, "Invalid json request, missing key: field")


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



    jsonOutput["TEST"] = DeconstructJson.deconstruct()


    #return str(fields)
    return json.dumps(jsonOutput)
