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

def negate(operation):
    op_dict = dict()
    op_dict['lt'] = 'gte'
    op_dict['gt'] = 'lte'
    op_dict['gte'] = 'lt'
    op_dict['lte'] = 'gt'
    op_dict['eq'] = 'ne'
    op_dict['ne'] = 'eq'
    return op_dict[operation]

