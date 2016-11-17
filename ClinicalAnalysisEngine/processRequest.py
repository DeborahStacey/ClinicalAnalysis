## processRequest.py
# Primary Owner: Russel Dunk
import jsonToSqlParms
import sqlParmsToQuery
import Cat
import json
import sql_utils

#####
##### ProcessRequest
#####
def ProcessRequest(dataInput):

    sqlParms = jsonToSqlParms.JsonToSqlParms(dataInput)
    if(type(sqlParms) == type(dict())): # if an error json is returned
        return json.dumps(sqlParms)

    sqlQuery = sqlParmsToQuery.sqlParmsToQuery(sqlParms, dataInput)

    sql_data = sql_utils.get_dict(sqlQuery)
    cats = Cat.sql_data_to_cats(sql_data)

    completedRequest = Cat.cats_to_json(cats)

    return completedRequest
