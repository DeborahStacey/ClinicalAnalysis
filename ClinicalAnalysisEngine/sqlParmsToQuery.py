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
            return query
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
        query = lookupPercentage(loadedJson, inputParms)

    return query


def lookupPercentage(loadedJson, inputParms):

    if 'group by' in loadedJson:
        groupBy = loadedJson['group by']

        equation = "((((pet.length/0.7062) - pet.height)/0.9156 ) - pet.height)"

        if groupBy == "bodyType":
            query = "SELECT count(*), CASE WHEN " + equation + " <= 25 THEN 'Low' WHEN " + equation + " > 25 AND " + equation + " <= 35 THEN 'Moderate' WHEN " + equation + " > 35 AND " + equation + " <= 45 THEN 'High' WHEN " + equation + " > 45 AND " + equation + " <= 55 THEN 'Serious' WHEN " + equation + " > 55 AND " + equation + " <= 65 THEN 'Severe' WHEN  " + equation + " > 65 THEN 'Extreme' END AS bodyType FROM pet"

            query = query + " WHERE " + inputParms

            query = query + " GROUP BY " + groupBy
            return query
