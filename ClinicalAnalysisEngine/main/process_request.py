## process_request.py
# Primary Owner: Andrew Downie

import json

def ProcessRequest(jsonRequest):
	loadedJson = json.loads(jsonRequest)
	print(loadedJson)
	return loadedJson['request']
