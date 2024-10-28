# the instructions
def show_instructions():
    print('''
        Welcome 
***** instructions ******

-The user chooses a shape by entering the corresponding letter.
s. Square - Calculate area and perimeter of a square.
r. Rectangle - Calculate area and perimeter of a rectangle.
t. Triangle - Calculate area of a triangle. Using heron's formula
c. Circle - Calculate area and perimeter of a circle.
When you have finished using the program, press 'No' to quit.

*************************''')


import math
import pandas as pd


# Show instructions
def show_instructions():
    print('''\
        Welcome 
***** Instructions ******

- Choose a shape by entering the corresponding letter:
s. Square - Calculate area and perimeter of a square.
r. Rectangle - Calculate area and perimeter of a rectangle.
t. Triangle - Calculate area of a triangle using Heron's formula.
c. Circle - Calculate area and perimeter of a circle.
- Press 'q' to quit the program at any time.

*************************''')


# Validate yes or no response
def yes_no(question):
    while True:
        response = input(question).lower()
        if response in ("yes", "y"):
            return True
        elif response in ("no", "n"):
            return False
        else:
            print("Please enter 'yes' or 'no'.")


# Calculate square area and perimeter
def square_calculation(side_length):
    area = side_length ** 2
    perimeter = 4 * side_length
    return area, perimeter


# Calculate rectangle area and perimeter
def rectangle_calculation(length, width):
    area = length * width
    perimeter = 2 * (length + width)
    return area, perimeter


# Calculate triangle area using Heron's formula, check validity
def triangle_calculation(a, b, c):
    if (a + b > c) and (a + c > b) and (b + c > a):
        s = (a + b + c) / 2
        area = math.sqrt(s * (s - a) * (s - b) * (s - c))
        perimeter = a + b + c
        return area, perimeter
    else:
        return None, None


# Calculate circle area and perimeter
def circle_calculation(radius):
    area = math.pi * radius ** 2
    perimeter = 2 * math.pi * radius
    return area, perimeter


# Check for valid number input
def num_checker(prompt):
    while True:
        try:
            number = float(input(prompt))
            if number > 0:
                return number
            else:
                print("Please enter a positive number.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")


# Main routine
def main():
    # Set up lists to store shape data
    shape_list = []
    area_list = []
    perimeter_list = []

    # Shape data dictionary
    variable_dict = {
        "Shapes": shape_list,
        "Area": area_list,
        "Perimeter": perimeter_list,
    }

    # Show instructions if user wants
    if yes_no("Do you want to read the instructions (yes/no)? "):
        show_instructions()

    # Start shape calculation loop
    while True:
        # Get user shape choice
        choice = input("Enter your choice (s/r/t/c or 'q' to quit): ").lower()

        # Exit option
        if choice == 'q':
            print("Exiting the program.")
            break

        # Square calculation
        if choice == "s":
            side_length = num_checker("Enter the side length of your square: ")
            area, perimeter = square_calculation(side_length)
            shape = "Square"

        # Rectangle calculation
        elif choice == "r":
            length = num_checker("Enter the length of the rectangle: ")
            width = num_checker("Enter the width of the rectangle: ")
            area, perimeter = rectangle_calculation(length, width)
            shape = "Rectangle"

        # Triangle calculation with validity check
        elif choice == "t":
            a = num_checker("Enter the length of the first side: ")
            b = num_checker("Enter the length of the second side: ")
            c = num_checker("Enter the length of the third side: ")
            area, perimeter = triangle_calculation(a, b, c)
            if area is None:
                print("The given sides do not form a valid triangle. Please try again.")
                continue
            shape = "Triangle"

        # Circle calculation
        elif choice == "c":
            radius = num_checker("Enter the radius of the circle: ")
            area, perimeter = circle_calculation(radius)
            shape = "Circle"

        else:
            print("Invalid choice. Please choose a valid shape.")
            continue

        # Append results to lists
        shape_list.append(shape)
        area_list.append(area)
        perimeter_list.append(perimeter)

        print(f"(Area: {area:.2f}, Perimeter: {perimeter:.2f})")

        # Ask if the user wants to calculate another shape
        if not yes_no("Do you want to calculate another shape (yes/no)? "):
            break

    # Create DataFrame and print results
    shape_data_frame = pd.DataFrame(variable_dict)
    shape_data_frame = shape_data_frame.set_index('Shapes')

    print("\n ***** -- SHAPE DATA -- *****")
    print(shape_data_frame)


# Run the main function
if __name__ == "__main__":
    main()

import math
import pandas


# The instructions
def show_instructions():
    print('''\
        Welcome 
***** instructions ******

-The user chooses a shape by entering the corresponding letter.
s. Square - Calculate area and perimeter of a square.
r. Rectangle - Calculate area and perimeter of a rectangle.
t. Triangle - Calculate area of a triangle using Heron's formula.
c. Circle - Calculate area and perimeter of a circle.
When you have finished using the program, press 'No' to quit.
Print the dataframe.

*************************''')


def yes_no(question):
    while True:
        response = input(question).lower()
        if response in ("yes", "y"):
            return True
        elif response in ("no", "n"):
            return False
        else:
            print("Please enter 'yes' or 'no'.")


# Calculate the area and perimeter of square
def square_calculation(side_length):
    area = side_length ** 2
    perimeter = 4 * side_length
    return area, perimeter


# Calculate the area and perimeter of the rectangle
def rectangle_calculation(length, width):
    area = length * width
    perimeter = 2 * (length + width)
    return area, perimeter


# Calculate the area of a triangle using Heron's formula
def triangle_calculation(a, b, c):
    s = (a + b + c) / 2
    area = math.sqrt(s * (s - a) * (s - b) * (s - c))
    perimeter = a + b + c
    return area, perimeter


# Calculate the area and perimeter of a circle
def circle_calculation(radius):
    area = math.pi * radius ** 2
    perimeter = 2 * math.pi * radius
    return area, perimeter


# Checks for a valid positive number
def num_checker(prompt):
    while True:
        try:
            number = float(input(prompt))
            if number > 0:
                return number
            else:
                print("Please enter a positive number.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")


# Main routine

# Set up lists
shape_list = []
area_list = []
perimeter_list = []
dimension_list = []

# Shape data
variable_dict = {
    "Shapes": shape_list,
    "Area": area_list,
    "Perimeter": perimeter_list,
    "Dimensions": dimension_list,
}

# Ask user if they want to see the instructions
want_instructions = yes_no("Do you want to read the instructions (y/n): ")
if want_instructions:
    show_instructions()

# Shape calculation
while True:
    # Tells the user to pick a shape
    choice = input("Enter your choice (s/r/t/c): ").lower()

    # Ask the user what side length they want and calculate
    if choice == "s":
        print("You chose square.")
        side_length = num_checker("Enter the side length of your square: ")
        area, perimeter = square_calculation(side_length)
        shape = "Square"
        dimensions = f"Side length: {side_length}"
        print(f"(Area: {area}, Perimeter: {perimeter})")

    # Ask the user what length and width they want and calculate
    elif choice == 'r':
        print("You chose rectangle.")
        length = num_checker("Enter the length of the rectangle: ")
        width = num_checker("Enter the width of the rectangle: ")
        area, perimeter = rectangle_calculation(length, width)
        shape = "Rectangle"
        dimensions = f"Length: {length}, Width: {width}"
        print(f"(Area: {area}, Perimeter: {perimeter})")

    # Ask the user for the lengths of the triangle's sides and calculate
    elif choice == 't':
        print("You chose triangle.")
        a = num_checker("Enter the length of the first side: ")
        b = num_checker("Enter the length of the second side: ")
        c = num_checker("Enter the length of the third side: ")
        area, perimeter = triangle_calculation(a, b, c)
        shape = "Triangle"
        dimensions = f"Sides: {a}, {b}, {c}"
        print(f"(Area: {area}, Perimeter: {perimeter})")

    # Ask the user what radius they want and calculate
    elif choice == 'c':
        print("You chose circle.")
        radius = num_checker("Enter the radius of the circle: ")
        area, perimeter = circle_calculation(radius)
        shape = "Circle"
        dimensions = f"Radius: {radius}"
        print(f"(Area: {area}, Perimeter: {perimeter})")

    else:
        print("Invalid choice. Please choose between s, r, t, and c.")
        continue

    # Append the results to the lists
    shape_list.append(shape)
    area_list.append(area)
    perimeter_list.append(perimeter)
    dimension_list.append(dimensions)

    # Ask if the user wants to continue
    want_other_shape = yes_no("Do you want to choose other shapes? (yes/no): ")
    if not want_other_shape:
        break

# Create dataframe and print it
shape_data_frame = pandas.DataFrame(variable_dict)
shape_data_frame = shape_data_frame.set_index('Shapes')

heading = "\n ***** -- SHAPE DATA -- *****"
print(heading)
print(shape_data_frame)
