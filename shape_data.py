import pandas


def yes_no(question):
    while True:
        response = input(question).lower()
        if response in ("yes", "y"):
            return True
        elif response in ("no", "n"):
            return False
        else:
            print("Please enter 'yes' or 'no'.")


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


shape_list = []
area_list = []
perimeter_list = []

while True:
    choice = input("Enter your choice (s/r): ").lower()
    if choice == "s":
        print("You chose square")
        side_length = num_checker("Enter the side length of your square: ")
        area = side_length ** 2
        perimeter = 4 * side_length
        shape = "square"
        print(f"Area: {area}, Perimeter: {perimeter}")

    elif choice == "r":
        print("You chose rectangle")
        length = num_checker("Enter the length of the rectangle: ")
        width = num_checker("Enter the width of the rectangle: ")
        area = length * width
        perimeter = 2 * (length + width)
        shape = "rectangle"
        print(f"Area: {area}, Perimeter: {perimeter}")

    else:
        print("Invalid choice. Please choose between 's' and 'r'.")
        continue

    # Ask if the user wants to continue
    want_other_shape = yes_no("Do you want to choose other shapes? (yes/no): ")
    if not want_other_shape:
        break

    # Append the results to the lists
    shape_list.append(shape)
    area_list.append(area)
    perimeter_list.append(perimeter)

# shape data
variable_dict = {
    "Shapes": shape_list,
    "Area": area_list,
    "Perimeter": perimeter_list,
}

print("\n ******** SHAPE DATA *******")
shape_data_frame = pandas.DataFrame(variable_dict)
shape_data_frame = shape_data_frame.set_index('Shapes')
print(shape_data_frame)
