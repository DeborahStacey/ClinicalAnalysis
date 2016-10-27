## Class: Animal
# Primary Owner: Andrew Downie

# This class needs to match the database schema


class BaseInfo(dict):


    ownerid = -1
    petid = -1
    name = "Fake Name"
    breedid = -1
    gender = -1
    microchip = False
    fitcat = False
    dateofbirth = 0
    weight = -1.0
    height = -1.0
    length = -1.0
    dateofdeath = 0
    reasonfordeath = "unknown"
    lastupdated = 0
    dateadded = 0

    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)



