## Class: Cat
# Primary Owner: Russell Dunk

from ClinicalAnalysisEngine import BaseInfo
from ClinicalAnalysisEngine import sql_utils


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


debug = ''

json = '{"cats": ['
cats = sql_utils.get_dict()
for cat in cats:
    json += debug + '{' + Cat(BaseInfo.BaseInfo(**cat)).json() + '}, '
json = json[:-2]
json += debug + "]}"

print(json)
