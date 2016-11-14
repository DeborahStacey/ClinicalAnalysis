## process_request.py
# Primary Owner: Cole Hoffele

import json
import standards

def sqlParmsToQuery(inputParms, dataInput):

    loadedJson = ""

    ###
    ### Load the Json request
    ###
    try:
        loadedJson = json.loads(dataInput)
    except:
    	return standards.InvalidJSON()

    query = AnalysisType(loadedJson, inputParms)
    return query


def AnalysisType(loadedJson, inputParms):

    operation = loadedJson['operation']

    if str(operation) == "correlation":
        if 'X-axis' in loadedJson:
            if 'Y-axis' in loadedJson:
                if 'X-interval' in loadedJson:
                    if 'Y-interval' in loadedJson:
                        query = correlationType(loadedJson, inputParms)
                        return query

    if type(operation) == type(list()):
        if operation[0] == "lookup":
            query = lookupType(loadedJson, inputParms)
    else:
        return "SELECT pet.weight FROM pet"



def correlationType(loadedJson, inputParms):

    xAxis = loadedJson['X-axis']
    yAxis = loadedJson['Y-axis']
    xInterval = loadedJson['X-interval']
    if str(xInterval) == "auto":
        xInterval = 5
    yInterval = loadedJson['Y-interval']
    if str(yInterval) == "auto":
        yInterval = 5

    query = "SELECT count(*) AS TOTAL,FLOOR(pet." + str(xAxis) + "/" + str(xInterval) + ") AS Interval FROM pet WHERE " + inputParms + " GROUP BY Interval ORDER BY Interval"
    return query



def lookupType(loadedJson, inputParms):

    operation = loadedJson['operation']

    if operation[1] == "percentage":
        query = lookupPercentage(loadedJson)

    return query


def lookupPercentage(loadedJson):

    query = ""
    if 'group by' in loadedJson:
        groupBy = loadedJson['group by']

        if groupBy == "bodyType":
            query = "SELECT count(*) AS TOTAL, FROM pet WHERE"
