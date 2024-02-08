# Importing a module
import pizza

pizza.make_pizzas("pepper")
pizza.make_pizzas("pepper", "chicken", "beef")

##########################################################

# Importing specific functions from a module
from pizza import make_pizzas

make_pizzas("pepper")
make_pizzas("pepper", "chicken", "beef")

##########################################################

# Using "as" to give a function an alias

from pizza import make_pizzas as mp

mp("pepper")
mp("pepper", "chicken", "beef")
