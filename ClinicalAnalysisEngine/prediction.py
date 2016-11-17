import json
import standards
import sql_utils

def Predict(loadedJson, inputParms):
    print('hello')

    id = loadedJson['field']['id']
    # given cat, want to know how likely it is to develop weight issues?????

    sql_data = sql_utils.get_dict("SELECT * FROM pet WHERE petid = " + str(id))

    #print(sql_data[0])

    gender = sql_data[0]['gender']
    weigth = sql_data[0]['weight']
    breed = sql_data[0]['breed']
    height = sql_data[0]['height']
    length = sql_data[0]['length']

    prediction_data = sql_utils.get_dict("SELECT AVG(weight) as weight, AVG(height) as height, AVG(length) as length FROM pet WHERE gender = " + str(gender) + " AND breed = " + str(breed))
    print(prediction_data)

    prediction_data = sql_utils.get_dict("SELECT weight FROM pet WHERE gender = " + str(gender) + " AND breed = " + str(breed))
    print(prediction_data)

    prediction_data = sql_utils.get_dict("SELECT 1.0 * (SELECT count(*) FROM pet WHERE gender = "+str(gender)+" AND breed = "+str(breed)+" AND weight > 14) / count(*) as overweight FROM pet WHERE gender = " + str(gender) + " AND breed = " + str(breed))
    print(prediction_data)

    # get average age of death for similar cats

    # get common diseases for similar cats

    # get average weight for similar cats

    # get average length for similar cats

    # get average height fro similar cats

    #

    #age_data = sql_utils.get_dict("SELECT avg(age) FROM pet")

    return "SELECT * FROM pet"
