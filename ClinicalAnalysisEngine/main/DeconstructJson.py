## DeconstructJson.py
# Primary Owner: Andrew Downie

import QueryBuilder

def deconstruct():
    queryList = []
    queryList.append(["$and","age","eq",5])
    queryList.append(["$and","weight","lt",20])
    #queryList.append(["$and.$or","height","eq",20])
    #queryList.append(["$and.$or","length","eq",20])

    queryList.sort()
    print (queryList)
    return QueryBuilder.build_query(queryList)
