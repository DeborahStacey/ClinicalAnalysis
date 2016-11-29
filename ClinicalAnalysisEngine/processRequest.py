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

    sql_data = sql_utils.get_dict(sqlQuery[0])
    cats = Cat.sql_data_to_cats(sql_data)

    # if statistical operation
    if len(sqlQuery) == 3:
        col = []
        for cat in cats:
            col.append(getattr(cat.base_info, sqlQuery[2]))
        return "{\"" + sqlQuery[2] + "\": " + str(sqlQuery[1](col)) + "}"

    else:
        completedRequest = Cat.cats_to_json(cats)

    return completedRequest
