# LEGASPI, LANA CAZANDRA U.
# BSCPE 1-5

# ASSIGNMENT 9: ABSTRACTION AND ENCAPSULATION

# PSEUDOCODE

# import Car from car_class
from car_class import Car
import time

# create a test car object
def main():
    carObject=Car(2022, "BMW")

    # accelerate five times, while displaying speed
    for i in range(5):
        time.sleep(0.4)
        carObject.accelerate()
        print("Car accelerating... | Current Speed:", carObject.speed_get())

    print("\n")

    # brake five times, while displaying speed
    for i in range(5):
        time.sleep(0.4)
        carObject.brake()
        print("Braking... | Current Speed:", carObject.speed_get())

# run program
main()
