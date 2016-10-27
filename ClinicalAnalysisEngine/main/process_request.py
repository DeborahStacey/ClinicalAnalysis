## process_request.py
# Primary Owner: Andrew Downie

import error_message
import json
import QueryBuilder

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
    ### Parse Json from tree to flat list
    ###
    jsonOutput = {}

    allLeaves = []
    ParseJsonBranch(fields, "", allLeaves)
    print(str(allLeaves))

    try:
        return QueryBuilder.build_query(allLeaves)
    except Exception as e:
        print(">>ERROR: " + str(e) + "\n")

    return "There was an error."



def ParseJsonBranch(jsonRequest, nodeOperators, allLeaves):
    try:
        if(type(jsonRequest) == type(dict())):
            for key, val in jsonRequest.items():
                if(str(key)[0] == "$"):
                    nodeOperators += str(key) + "."
                    ParseJsonBranch(val, nodeOperators, allLeaves)
                else:
                    allLeaves.append(PackageJsonLeaf(nodeOperators, jsonRequest))
                    return
        elif(type(jsonRequest) == type(list())):
            listIndex = 0
            for item in jsonRequest:
                ParseJsonBranch(item, nodeOperators + str(listIndex) + ".", allLeaves)
                listIndex = listIndex + 1

    except Exception as e:
        print(">>ERROR: " + str(e) + "\n")
        return

def PackageJsonLeaf(nodeOperators, jsonLeaf):
    deconstructedLine = []

    curNode = ".".join(nodeOperators.split(".")[:-2])

    try:
        for topKey, topVal in jsonLeaf.items():
            for botKey, botVal in topVal.items():
                deconstructedLine = [curNode, topKey, botKey, botVal]
    except Exception as e:
        print(">>ERROR: " + str(e) + "\n")

    return deconstructedLine
