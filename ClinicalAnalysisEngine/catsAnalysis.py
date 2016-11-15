import sys
import processRequest


def AnalysisType(dataInput):




#######

    loadedJson = ""


    ###
    ### Load the Json request
    ###
    try:
        loadedJson = json.loads(jsonRequest)
    except:
    	return standards.InvalidJSON()


    ###
    ### Check that required keys are present
    ###
    if 'operation' not in loadedJson:
    	return standards.MissingOperation()
    elif 'animals' not in loadedJson:
    	return standards.MissingAnimal()
    elif 'field' not in loadedJson:
    	return standards.MissingField()


    ###
    ### Collect values of required keys
    ###
    operation = loadedJson['operation']
    animals = loadedJson['animals']
    fields = loadedJson['field']


    sqlParms = ParseGroupBy(operation)


    return sqlParms
    
#####

def ParseGroupBy(operation):


    f = open('myfile','w')
    f.write(operation) # python will convert \n to os.linesep
    f.close() # you can omit in most cases as the destructor will call it

    return dataInput
