## Class: Animal
# Primary Owner: Andrew Downie
class BaseInfo(object):

    name = "Base Name Value"
    species = "Base Species Value"
    breed = "Base Breed Value"
    gender = "Base Gender Value"
    colour = "Base Colour Value"
    age = "Base Age Value"
    sex = "Base Sex Value"
    weight = "Base Weight Value"
    height = "Base Height Value"
    length = "Base Length Value"
    owner_id = "Base owner id"
    animal_id = "Base animal id"
    microchip = "Base microchip"
    data_of_birth = "Base birthdate"

    def __init__(self, name=None, species=None, breed=None, gender=None, colour=None, age=None, sex=None, weight=None, height=None, length=None):
        self.name = name


    def __str__(self):
        return self.name
