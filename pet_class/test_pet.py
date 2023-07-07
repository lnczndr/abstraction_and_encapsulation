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

    animal_kind = input(str("What kind of pet do you have? : "))
    user_pet.kind_set(animal_kind)

    age = input(str("What is the age of your pet? : "))
    user_pet.age_set(age)

    # displays the pet details via output
    print("\nYour pet's name:", user_pet.name_get())
    print("Your pet's kind:", user_pet.kind_get())
    print("Your pet's age:", user_pet.age_get())
    
# run code
main()