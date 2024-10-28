def choose_shape():
    while True:
        print("Which shape would you like to choose?"
              " 1. Square, 2. Rectangle, 3. Triangle, 4. Circle)")

        try:
            user_choice = int(input("Enter your choice (1-4): "))

            if user_choice == 1:
                print("You chose square.")
            elif user_choice == 2:
                print("You chose rectangle.")
            elif user_choice == 3:
                print("You chose triangle.")
            elif user_choice == 4:
                print("You chose circle")
            else:
                print("Invalid choice. Please choose between 1 and 4.")
                print("What would you like to know?")

        except ValueError:
            print("Invalid input. Please enter a number (1-4).")

        # Ask the user if they want to choose another shape
        try_again = input("Do you want to choose another shape? (yes/no): ").lower()
        if try_again != 'yes':
            break


# Call the function to start choosing a shape
choose_shape()
