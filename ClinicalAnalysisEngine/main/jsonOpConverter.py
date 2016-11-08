## jsonOpConverter.py
# Primary Owner: Andrew Downie

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
        return "Error4: Invalid Operator"
    except Exception as e:
        print(">>ERROR5: " + str(e) + "\n")