import pandas


def num_check(question, error, num_type):
    valid = False

    while not valid:

        try:
            response = num_type(input(question))

            if response <= 0:
                print(error)
            else:
                return response

        except ValueError:
            print(error)


def not_blank(question, error):
    valid = False
    while not valid:
        response = input(question)

        if response == "":
            print("{}.  \nPlease try again.\n".format(error))
            continue

        return response


# currency formatting function
def currency(x):
    return "${:.2f}".format(x)


# Get expenses, returns list which has
# the data frame and subtotal
def get_expenses():
    # Set up dictionaries and lists

    item_list = []
    quantity_list = []
    price_list = []

    variable_dict = {
        "Item": item_list,
        "Quantity": quantity_list,
        "Price": price_list,
    }

    # loop to get component, quantity and price
    item_name = ""
    while item_name.lower() != "xxx":

        print()
        # get name, quantity and item
        item_name = not_blank("item name:", "The component name can't be blank.")
        if item_name.lower() == "xxx":
            break

        quantity = num_check("Quantity:",
                             "The amount must be a whole number "
                             "more than zero",
                             int)
        price = num_check("How much for a single item? $",
                          "The price must be a number <more "
                          "than 0>",
                          float)

        # add item, quantity and price to lists
        item_list.append(item_name)
        quantity_list.append(quantity)
        price_list.append(price)

    expense_frame = pandas.DataFrame(variable_dict)
    expense_frame = expense_frame.set_index('Item')

    # Calculate cost of each component
    expense_frame['Cost'] = expense_frame['Quantity'] * expense_frame['Price']

    # Find subtotal
    sub_total = expense_frame['Cost'].sum()

    # Currency Formatting (uses currency function)
    add_dollars = ['Price', 'Cost']
    for item in add_dollars:
        expense_frame[item] = expense_frame[item].apply(currency)

        return [expense_frame, sub_total]


# *** Main routine starts here ***

# Get product name
product_name = not_blank("Product name : ", "The product name ca")

variable_expenses = get_expenses()
variable_frame = variable_expenses[0]
variable_sub = variable_expenses[1]

# *** Printing Area ****

print()
print(variable_frame)
print()
