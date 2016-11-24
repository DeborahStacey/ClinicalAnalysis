import json
import standards
import sql_utils

def Predict(loadedJson, inputParms):

    id = loadedJson['field']['id']
    query = loadedJson['operation'][1]

    sql_data = sql_utils.get_dict("SELECT * FROM pet WHERE petid = " + str(id))

    gender = str(sql_data[0]['gender'])
    weight = str(sql_data[0]['weight'])
    breed = str(sql_data[0]['breed'])
    height = str(sql_data[0]['height'])
    length = str(sql_data[0]['length'])

    if(query=="physical"):
        return PredictPhysicalCharacteristics(gender, breed)
    if(query=="lifespan"):
        return PredictLifespan(gender,breed,weight,height,length)
    if(query=="sickness"):
        return PredictSickness(id)
    if(query=="disease"):
        return PredictDiseases()

    return "SELECT * FROM pet"

def PredictDiseases():
    return "SELECT * FROM pet"

def PredictPhysicalCharacteristics(gender, breed):
    # Find average weight, height and length
    return "SELECT AVG(weight) as weight, AVG(height) as height, AVG(length) as length FROM pet WHERE gender = " + gender + " AND breed = " + breed

def PredictLifespan(gender, breed, weight, height, length):
    # Find average age of death
    return ("SELECT DATE_PART('day', dateofdeath::timestamp - dateofbirth::timestamp)" +
        " FROM pet WHERE gender = " + gender +
        " AND breed = " + breed + " AND dateofdeath IS NOT NULL" +
        " AND " + SimilarHeights(height) +
        " AND " + SimilarWeights(weight) +
        " AND " + SimilarLengths(length))

def PredictOverweight(gender, breed, height, length):
    # Find percentage of similar cats that are overweight
    return ("SELECT 1.0 * (SELECT count(*) FROM pet WHERE gender = "+gender+
        " AND breed = "+breed+" AND weight > 14) / count(*) as overweight" +
        " FROM pet WHERE gender = " + gender + " AND breed = " + breed + " " +
        " AND " + SimilarHeights(height) +
        " AND " + SimilarLengths(length))


def PredictLifespanPerRegion():
    # as a vet, I want to know if cats from Ontario are more likely to live at least 10 years
    ontario_data = sql_utils.get_dict("SELECT (SELECT count(*) FROM pet WHERE DATE_PART('year', dateofdeath::timestamp - dateofbirth::timestamp) >= 10 AND region = 'Ontario')/count(*) AS OverTen FROM pet WHERE region = 'Ontario'")
    total_data = sql_utils.get_dict("SELECT (SELECT count(*) FROM pet WHERE DATE_PART('year', dateofdeath::timestamp - dateofbirth::timestamp) >= 10)/count(*) AS OverTen FROM pet")
    print(prediction_data)

def PredictSickness(id):
    return ("SELECT LEAST((weight/100 + (DATE_PART('year', CURRENT_TIMESTAMP - dateofbirth::timestamp) / 20)), 100) as SicknessPredictor" +
        " FROM pet WHERE petid = " + str(id))
    print(sickness_predictor)

def SimilarWeights(weight):
    return "weight > " + str(float(weight) * 0.95) + " AND weight < " + str(float(weight) * 1.05) + " "

def SimilarHeights(height):
    return "height > " + str(float(height) * 0.95) + " AND height < " + str(float(height) * 1.05) + " "

def SimilarLengths(length):
    return "length > " + str(float(length) * 0.95) + " AND length < " + str(float(length) * 1.05) + " "
