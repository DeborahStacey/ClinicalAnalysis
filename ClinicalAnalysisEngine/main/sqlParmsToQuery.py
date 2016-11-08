## process_request.py
# Primary Owner: Cole Hoffele


def sqlParmsToQuery(inputParms):

    query = "SELECT * FROM pet WHERE " + inputParms
    return query
