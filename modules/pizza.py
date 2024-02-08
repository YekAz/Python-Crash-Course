def make_pizzas(*toppings):
    # print the pasteries selected by the user
    print("\nMaking a pizza with the following toppings:")
    for topping in toppings:
        pizzas = print("-", topping)
    return pizzas
