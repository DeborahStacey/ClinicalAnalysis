## logging.py
# Primary Owner: Andrew Downie 


from time import gmtime, strftime

def LogTime():
    return strftime("%Y-%m-%d %H:%M:%S", gmtime()) + " GMT"
    

def Log(message):
    return '[' + LogTime() + '] ' + message 

def PrintLog(message):
    print(Log(message))
    

