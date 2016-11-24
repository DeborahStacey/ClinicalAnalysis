## process_request.py
# Primary Owner: Cole Hoffele

import json
import standards
import prediction

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
        if(operation[0] == "prediction"):
            query = prediction.Predict(loadedJson, inputParms)
            return query
    else:
        return "SELECT * FROM pet"



def correlationType(loadedJson, inputParms):

    xAxis = loadedJson['X-axis']
    yAxis = loadedJson['Y-axis']
    xInterval = loadedJson['X-interval']
    if str(xInterval) == "auto":
        xInterval = 5
    yInterval = loadedJson['Y-interval']
    if str(yInterval) == "auto":
        yInterval = 5

    query = "SELECT count(*) AS TOTAL,FLOOR(pet." + str(xAxis) + "/" + str(xInterval) + ") AS Interval FROM pet"
    query = buildQuery(query, inputParms, "Interval", "Interval")

    return query



def lookupType(loadedJson, inputParms):

    operation = loadedJson['operation']

    if operation[1] == "percentage":
        query = lookupPercentage(loadedJson, inputParms)
    elif operation[1] == "average":
        query = lookupAverage(loadedJson, inputParms)
    return query


def lookupPercentage(loadedJson, inputParms):

    if 'group by' in loadedJson:
        groupBy = loadedJson['group by']

        equation = "((((pet.length/0.7062) - pet.height)/0.9156 ) - pet.height)"

        if groupBy == "bodyType":
            query = "SELECT (CAST((((count(*) *1.0) / ( SELECT (COUNT(*) * 1.0) FROM pet )) *100) AS DECIMAL(10,2))) as percentage, count(*) as Count, CASE WHEN " + equation + " <= 25 THEN 'Low' WHEN " + equation + " > 25 AND " + equation + " <= 35 THEN 'Moderate' WHEN " + equation + " > 35 AND " + equation + " <= 45 THEN 'High' WHEN " + equation + " > 45 AND " + equation + " <= 55 THEN 'Serious' WHEN " + equation + " > 55 AND " + equation + " <= 65 THEN 'Severe' WHEN  " + equation + " > 65 THEN 'Extreme' END AS bodyType FROM pet"

            query = buildQuery(query, inputParms, groupBy, None)

            return query

def lookupAverage(loadedJson, inputParms):
    if loadedJson['operation'][2] != '':

        averaged = "AVG(" + loadedJson['operation'][2] + ") as avg_" + loadedJson['operation'][2]
        groupBy = loadedJson['group by']

        query = "SELECT " + groupBy + ", " + averaged + "  FROM pet"

        query = buildQuery(query, inputParms, groupBy, None)
        return query

#Use this function after you build the "SELECT" part of the query, and nothing else.
def buildQuery(query, inputParms, groupBy, orderBy):

    if query != None:
        if inputParms != None:
            query = whereClause(query,inputParms)
        if groupBy != None:
            query = groupByClause(query, groupBy)
        if orderBy != None:
            query = orderByClause(query, orderBy)
    else:
        print("Query not valid")

    return query


def groupByClause (query, groupBy):
    return query + " GROUP BY " + groupBy

def whereClause (query, inputParms):
    return query + " WHERE " + inputParms

def orderByClause (query, orderBy):
    return query + " ORDER BY " + orderBy






#
#SELECT CAST(field1 AS DECIMAL(10,2)) field1
