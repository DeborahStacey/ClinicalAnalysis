#!/usr/bin/env python

import sql_utils
import json_parser
import Cat

# Temporarily Hardcoded JSON

j = json_parser.ui_input_stub('{"animals": "all", "operation": "lookup", "field": "name"}')

# Temporary hack to output json
output = ""
data = sql_utils.get_all()
animals = []
for item in data:
    animals.append(Cat.Cat())
    animals[-1].baseInfo.name = item[1]
if j["field"] == "name":
    output = '{"' + j["field"] + '": ['
    for animal in animals:
        output += '"' + str(animal.baseInfo.name) + '", '
    # Chomp last two chars
    output = output[:-2]
    output += ']}'
print(output)

