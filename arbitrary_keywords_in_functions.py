# Passing an arbitarary or unknown number of arguments into a function
def pizza(*toppings):
    # print the pasteries selected by the user
    pizzas = print(toppings)
    return pizzas

pizza("pepper")
pizza("pepper", "chicken", "beef")

# Replacing the print() with a loop that runs through the list of toppings

def pizza(*toppings):
    # print the pasteries selected by the user
    print("\nMaking a pizza with the following toppings:")
    for topping in toppings:
        pizzas = print("-", topping)
    return pizzas

pizza("pepper")
pizza("pepper", "chicken", "beef")