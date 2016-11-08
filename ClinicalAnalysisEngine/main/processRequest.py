## processRequest.py
# Primary Owner: Russel Dunk
import jsonToSqlParms
import sqlParmsToQuery

#####
##### ProcessRequest
#####
def ProcessRequest(dataInput):

    sqlParms = jsonToSqlParms.JsonToSqlParms(dataInput)

    sqlQuery = sqlParmsToQuery.sqlParmsToQuery(sqlParms)

    return sqlParms
