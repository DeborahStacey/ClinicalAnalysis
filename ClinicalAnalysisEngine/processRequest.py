## processRequest.py
# Primary Owner: Russel Dunk
import jsonToSqlParms
import sqlParmsToQuery
import Cat
import sql_utils

#####
##### ProcessRequest
#####
def ProcessRequest(dataInput):

    sqlParms = jsonToSqlParms.JsonToSqlParms(dataInput)

    sqlQuery = sqlParmsToQuery.sqlParmsToQuery(sqlParms, dataInput)

    sql_data = sql_utils.get_dict(sqlQuery)
    cats = Cat.sql_data_to_cats(sql_data)

    completedRequest = Cat.cats_to_json(cats)

    return completedRequest
