"""An attempt to import the Resaturant class from the restaurant_module"""

from restaurant_module import Restaurant

pizza = Restaurant("PizzaHut", "African-Pizza")
pizza.describe_restaurant()
pizza.open_restaurant()
pizza.number_served_count()

pizza.number_served = 5
pizza.number_served_count()

pizza.set_number_served(17)
pizza.number_served_count()

pizza.increment_number_served(3)
pizza.number_served_count()

