## jsonOpConverter.py
# Primary Owner: Andrew Downie

import standards

def Convert(operation):
    try:
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
        return standards.InvalidOperation()
    except Exception as e:
        print(standards.CaughtException(str(e)))
