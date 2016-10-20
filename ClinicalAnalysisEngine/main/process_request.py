## process_request.py
# Primary Owner: Andrew Downie

import json

def ProcessRequest(jsonRequest):
	loadedJson = ""

	try:
	    loadedJson = json.loads(jsonRequest)
	    return loadedJson['operation']
	except:
            return("Not valid json request, missing operation key")
