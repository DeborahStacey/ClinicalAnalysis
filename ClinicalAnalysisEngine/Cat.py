## Class: Cat
# Primary Owner: Russell Dunk

import BaseInfo
import sql_utils


class Cat:

    def __init__(self, base_info):
        self.base_info = base_info

    def __str__(self):
        print(self.base_info.name)

    # Excludes outer brackets
    def json(self):
        json = ""
        class_vars = vars(self.base_info)
        for key in class_vars:
            json += '"' + key + '":' + '"' + str(class_vars[key]) + '", '
        return json[:-2]



def sql_data_to_cats(sql_data):
    cats = []
    for cat in sql_data:
        cats.append(Cat(BaseInfo.BaseInfo(**cat)))
    return cats


def cats_to_json(cats):
    # Debug allows for newlines in keyplaces in json
    debug = ''
    json = '{"cats": ['
    for cat in cats:
        json += debug + '{' +  cat.json() + '}, '
    json = json[:-2]
    json += debug + "]}"
    return json
