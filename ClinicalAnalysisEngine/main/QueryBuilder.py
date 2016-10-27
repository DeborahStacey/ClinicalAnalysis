## QueryBuilder.py
# Primary Owner: Cole Hoffele

nodeOperators = 0
field = 1
operator = 2
value = 3

def build_query(queryList):

    sqlWhere = "("
    firstBracket = True
    openBracket = False

    for i in range (0, len(queryList)):
        node = queryList[i]
        if(i != 0):
            lastNode = queryList[i-1]
            if(node[nodeOperators] != lastNode[nodeOperators]):
                if(firstBracket == False):
                    sqlWhere += ")"
                    openBracket = False
                firstBracket = False
                sqlWhere += "("
                openBracket = True

        sqlWhere += parameterBuilder(node)

        if(i < len(queryList)-1):
            sqlWhere += lastNodeOperator(node)

    if(openBracket == True):
        sqlWhere += ")"

        #print (node)

    sqlWhere += ")"

    #print (sqlWhere)
    return sqlWhere


def parameterBuilder(node):
    parameter = ""
    print (node[field])
    parameter += node[field]
    parameter += operationConverter(node)
    parameter += valueConverter(node)
    return parameter

def operationConverter(node):
    operation = node[operator]
    if(operation == "lt"):
        return "<"
    elif (operation == "gt"):
        return ">"
    elif (operation == "eq"):
        return "="
    elif (operation == "ne"):
        return "!="
    elif (operation == "lte"):
        return "<="
    elif (operation == "gte"):
        return ">="
    return "Error: Invalid Operator"

def valueConverter(node):
    val = node[value]

    if(isinstance(val, str)):
        return "'"+str(val)+"'"
    elif(isinstance(val, int)):
        return str(val)
    elif(isinstance(val,float)):
        return str(val)

    return "Error: Invalid value type(" + str(val) + ")"

def lastNodeOperator(node):
    return " " + node[nodeOperators].split(".")[-1][1:].upper() + " "
