import json
import standards
import sql_utils

def Predict(loadedJson, inputParms):

    id = loadedJson['field']['id']
    # given cat, want to know how likely it is to develop weight issues?????

    sql_data = sql_utils.get_dict("SELECT * FROM pet WHERE petid = " + str(id))

    #print(sql_data[0])

    gender = str(sql_data[0]['gender'])
    weigth = str(sql_data[0]['weight'])
    breed = str(sql_data[0]['breed'])
    height = str(sql_data[0]['height'])
    length = str(sql_data[0]['length'])

    # Find average weight, height and length
    prediction_data = sql_utils.get_dict("SELECT AVG(weight) as weight, AVG(height) as height, AVG(length) as length FROM pet WHERE gender = " + gender + " AND breed = " + breed)
    print(prediction_data)

    # Just getting weights to ensure percentage is right
    prediction_data = sql_utils.get_dict("SELECT weight FROM pet WHERE gender = " + gender + " AND breed = " + breed)
    print(prediction_data)

    # Find percentage of similar cats that are overweight
    prediction_data = sql_utils.get_dict("SELECT 1.0 * (SELECT count(*) FROM pet WHERE gender = "+gender+" AND breed = "+breed+" AND weight > 14) / count(*) as overweight FROM pet WHERE gender = " + gender + " AND breed = " + breed)
    print(prediction_data)

    # Find average age of death
    prediction_data = sql_utils.get_dict("SELECT dateofdeath, dateofbirth FROM pet WHERE gender = " + gender + " AND breed = " + breed + " AND dateofdeath IS NOT NULL")
    print(prediction_data)

    # get average age of death for similar cats

    # get common diseases for similar cats



    return "SELECT * FROM pet"
