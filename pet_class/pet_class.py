# LEGASPI, LANA CAZANDRA U.
# BSCPE 1-5

# ASSIGNMENT 9: ABSTRACTION AND ENCAPSULATION

# PSEUDOCODE

# making pet class
class Pet:

    # using constructor to assign values
    def __init__(self):
        self.__name=""
        self.__animal_kind=""
        self.__age= 0

    # specifying name of the pet
    # set name of the pet
    def name_set(self, name):
        self.__name = name

    # get name of the pet
    def name_get(self):
        return self.__name

    # specifying the kind of  pet
    # set kind of pet
    def kind_set(self, animal_kind):
        self.__animal_kind = animal_kind
    
    # get kind of pet
    def kind_get(self):
        return self.__animal_kind

    # specifying the age of the pet
    # set age of the pet
    def age_set(self, age):
        self.__age = age
    
    # get age of the pet
    def age_get(self):
        return self.__age
