# LEGASPI, LANA CAZANDRA U.
# BSCPE 1-5

# ASSIGNMENT 9: ABSTRACTION AND ENCAPSULATION

# PSEUDOCODE

# import pet from pet_class
from pet_class import Pet
def main():
    # create a pet object 
    user_pet = Pet()

    # ask user for input regarding the details of the pet
    name = input(str("What is your pet's name? : "))
    user_pet.name_set(name)


# displays the pet details via output