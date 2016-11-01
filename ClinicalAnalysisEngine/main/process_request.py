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


    sqlQuery = ParseJsonBranch(fields, None)
    print(sqlQuery)
    return "Premature exit"

    try:
        return QueryBuilder.build_query(allLeaves)
    except Exception as e:
        print(">>ERROR1: " + str(e) + "\n")

    return "There was an error."


def ParseJsonBranch(jsonBranch, lastOperator):
    try:
        if(type(jsonBranch) == type(dict())):
            for key, val in jsonBranch.items():
                if(str(key)[0] == "$"):
                    print(str(key)[1:])
                    return ParseJsonBranch(val, str(key)[1:])
                else:
                    return JsonToSqlParm(jsonBranch)
        elif(type(jsonBranch) == type(list())):
            sqlPiece = "("
            for i in range(0, len(jsonBranch)):
                sqlPiece += ParseJsonBranch(jsonBranch[i], lastOperator)
                if(i < len(jsonBranch)-1):
                    sqlPiece += " " + str(lastOperator) + " "


            sqlPiece += ")"
            return sqlPiece

    except Exception as e:
        print(">>ERROR2: " + str(e) + "\n")
        return



def JsonToSqlParm(jsonLeaf):
    try:
        for field, jsonKeyVal in jsonLeaf.items():
            for operator, value in jsonKeyVal.items():
                print(str(operator) + " " + str(value))
                return str(field) + " " + operationConverter(operator) + " " + str(value)
    except Exception as e:
        print(">>ERROR3: " + str(e) + "\n")



def operationConverter(operation):
    try:
        if(operation == "lt"):
            return "<"
        elif (operation == "gt"):
            return ">"
        elif (operation == "eq"):
            return "="
        elif (operation == "ne"):
            return "!="
        elif (operation == "lte"):
            return "<="
        elif (operation == "gte"):
            return ">="
        return "Error4: Invalid Operator"
    except Exception as e:
        print(">>ERROR5: " + str(e) + "\n")
