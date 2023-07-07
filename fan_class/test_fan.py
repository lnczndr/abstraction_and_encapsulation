# LEGASPI, LANA CAZANDRA U.
# BSCPE 1-5

# ASSIGNMENT 9: ABSTRACTION AND ENCAPSULATION

# PSEUDOCODE

# import class
from fan_class.fan_class import Fan

# defining main method
def main():
    # assign values for fan 1
    fan1 = Fan(Fan.FAST, 10, "yellow", True)
    
    # assign values for fan 2
    fan2 = Fan(Fan.MEDIUM, 5, "blue", False)

    # output:
    # fan 1
    print("Fan 1:")
    print("Fan Speed:", fan1.speed_get())
    print("Fan Radius:", fan1.radius_get())
    print("Fan Color:", fan1.color_get())
    print("On:", fan1.is_on())

    # fan 2
    print("\nFan 2:")
    print("Fan Speed:", fan2.speed_get())
    print("Fan Radius:", fan2.radius_get())
    print("Fan Color:", fan2.color_get())
    print("On:", fan2.is_on())
