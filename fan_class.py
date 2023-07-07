# LEGASPI, LANA CAZANDRA U.
# BSCPE 1-5

# ASSIGNMENT 9: ABSTRACTION AND ENCAPSULATION

# PSEUDOCODE

# making fan class
class Fan:

# assigning values to 3 constants (slow, medium, fast)
    SLOW = 1
    MEDIUM = 2
    FAST = 3

    # using constructor to assign values
    def __init__ (self, speed = 1, radius = 5, color = "Blue", on = False):
        self.__speed = speed
        self.__on = on
        self.__radius = radius
        self.__color = color

    # setting the speed of the fan
    def speed_set (self, speed):
        self.__speed = speed

    # getting the speed of the fan
    def speed_get (self):
        return self.__speed

    # specifying if the fan is on/off
    def is_on(self):
        return self.__on
    
    # specifying the radius of the fan

    # specifying the color of the fan

    # implementing getter and setter for four data fields

