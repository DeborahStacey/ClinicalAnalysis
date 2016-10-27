## DeconstructJson.py
# Primary Owner: Andrew Downie

import QueryBuilder

def deconstruct(jsonRequest):
    allLeaves = []
    ParseJsonBranch(jsonRequest["field"], "", allLeaves)
    print(str(allLeaves))

    try:
        return QueryBuilder.build_query(allLeaves)
    except Exception as e:
        print(">>ERROR: " + str(e) + "\n")

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
